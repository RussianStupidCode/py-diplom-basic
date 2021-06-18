import requests
from api.photos.vk.extractor import ExtractorVK
from api.photos.ok.extractor import ExtractorOK
from api.storage.ya_disk.loader import YaUploader
from converter.photos_vk import ConverterVK
from converter.photos_ok import ConverterOK


def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Ошибка при получении изображения по адресу {url}")
    return response.content


class PhotosKeeper:
    """
    Класс с основной логикой загрузки
    и сохранения фото для пользователя
    """

    def __init__(self):
        self.ya_disk = None
        self.ok = ExtractorOK()
        self.vk = ExtractorVK()

    def __save_photo(self, photo, storage_path):
        result = {}
        try:
            content = load_image(photo.url)
            self.ya_disk.upload(photo.file_name, content, storage_path)
        except (RuntimeError, ValueError) as ex:
            result['error'] = ex
        finally:
            result['info'] = photo
        return result

    def __save_photos(self, refined_photos, storage_path):
        success = []
        fails = []
        for photo in refined_photos:
            print(f"Сохранение фото с именем {photo.file_name} в директории {storage_path}")

            info = self.__save_photo(photo, storage_path)

            if 'error' in info:
                fails.append(info)
                print(f"ошибка сохранения фото {info['error']}")
            else:
                success.append(info)
                print(f"Фото сохранено успешно")

        return success, fails

    def check_storage_valid(self):
        if self.ya_disk is None or not self.ya_disk.is_valid_token():
            raise ValueError(f"Не инициализировано хранилище фотографий")

    def save_yandex_token(self, token):
        self.ya_disk = YaUploader(token)
        if not self.ya_disk.is_valid_token():
            raise ValueError(f"Невалидный токен для яндекс диска {token}")

    def query_save_photos_vk(self, id_user, photo_count=5):
        self.check_storage_valid()

        photos = self.vk.get_photos(id_user)
        refined_photos = ConverterVK.convert(photos, photo_count)
        storage_path = f"vk_{id_user}"
        self.ya_disk.make_directory(storage_path)
        return self.__save_photos(refined_photos, storage_path)

    def query_save_photos_ok(self, id_user, photo_count=5):
        self.check_storage_valid()

        photos = self.ok.get_photos(id_user)
        refined_photos = ConverterOK.convert(photos, photo_count)
        storage_path = f"ok_{id_user}"
        self.ya_disk.make_directory(storage_path)
        return self.__save_photos(refined_photos, storage_path)


