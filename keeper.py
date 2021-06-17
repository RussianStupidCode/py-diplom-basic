import requests
from api.photos.vk.extractor import ExtractorVK
from api.photos.ok.extractor import ExtractorOK
from api.storage.ya_disk.loader import YaUploader
from converter.photos_vk import ConverterVK
from converter.photos_ok import ConverterOK


def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Ошибка при получении изображения по адресу {response.status_code}")
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
            result = {
                'info': photo
            }
        except Exception as ex:
            result = {
                'info': photo,
                'error': ex
            }
        return result

    def __save_photos(self, refined_photos, storage_path):
        success = []
        fails = []
        for photo in refined_photos:
            print(f"Сохранение фото с именем {photo.file_name} в директории {storage_path}")

            info = self.__save_photo(photo, storage_path)

            if 'error' in info:
                print(f"ошибка сохранения фото {info['error']}")
            else:
                print(f"Фото сохранено успешно")

        return success, fails

    def is_storage_valid(self):
        if self.ya_disk is None or not self.ya_disk.is_valid_token():
            raise ValueError(f"Не инициализировано место хранения фото")

    def save_yandex_token(self, token):
        self.ya_disk = YaUploader(token)
        if not self.ya_disk.is_valid_token():
            raise ValueError(f"Невалидный токен для яндекс диска {token}")

    def query_save_photos_vk(self, id_user, photo_count=5):
        params = {
            'album_id': 'profile',
        }
        photos = self.vk.get_photos(id_user, **params)
        refined_photos = ConverterVK.convert(photos, photo_count)
        storage_path = f"vk_{id_user}"

        self.ya_disk.make_directory(storage_path)
        return self.__save_photos(refined_photos, storage_path)

    def query_save_photos_ok(self, id_user, photo_count=5):
        photos = self.ok.get_photos(576783256198)
        refined_photos = ConverterOK.convert(photos, photo_count)
        storage_path = f"ok_{id_user}"

        self.ya_disk.make_directory(storage_path)
        return self.__save_photos(refined_photos, storage_path)


