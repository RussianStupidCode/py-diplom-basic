from api import ApiVK


class ExtractorVK:
    def __init__(self, api):
        self.api = api

    def get_photos(self, **params):
        method = 'photos.get'
        default_params = {'extended': 1, **params}
        content = self.api.get(method, **default_params).json()

        if 'error' in content:
            raise ValueError(f'Некорретные данные запроса фотографии: {content}')

        return content


if __name__ == "__main__":
    vk = ApiVK()
    params = {
        'owner_id': 552934290,
        'album_id': 'profile',
    }
    extractor = ExtractorVK(vk)
    print(extractor.get_photos(**params))
