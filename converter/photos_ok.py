try:
    from photo_info import PhotoInfo
except ImportError:
    from converter.photo_info import PhotoInfo

MILLISECONDS_TO_SECONDS = 1000


class ConverterOK:

    @staticmethod
    def __create_photo_info(photo):
        date = photo['created_ms']
        likes_count = photo['like_count']

        return PhotoInfo(f'{likes_count}_{date}.png', photo['standard_height'],
                         photo['standard_width'], photo['pic_max'], )

    @staticmethod
    def convert(response_content, max_count=5):
        """Возвращает список данных о фотографий в общем формате"""

        photos_info = []
        album_info = response_content['photos']

        for photo in album_info:
            info = ConverterOK.__create_photo_info(photo)
            photos_info.append(info)

        photos_info.sort(key=lambda p: p.height * p.width, reverse=True)

        return photos_info[:max_count]
