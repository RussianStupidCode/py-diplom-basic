try:
    from photo_info import PhotoInfo
except ImportError:
    from converter.photo_info import PhotoInfo


class ConverterVK:

    @staticmethod
    def __create_photo_info(photos):
        date = photos['date']
        likes_count = photos['likes']['count']
        most_big_photo = max(photos['sizes'], key=lambda p: p['height'] * p['width'])

        return PhotoInfo(f'{likes_count}_{date}.png', most_big_photo['height'],
                         most_big_photo['width'], most_big_photo['url'], )

    @staticmethod
    def convert(response_content, max_count=5):
        """Возвращает список данных о фотографий в общем формате"""

        photos_info = []
        album_info = response_content['response']['items']

        for photos in album_info:
            info = ConverterVK.__create_photo_info(photos)
            photos_info.append(info)

        photos_info.sort(key=lambda p: p.height * p.width, reverse=True)

        return photos_info[:max_count]
