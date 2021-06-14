from api import ApiVK


class ExtractorVK:
    def __init__(self, api):
        if not isinstance(api, ApiVK):
            raise NotImplemented
        self.api = api

    def get_photos(self, user_id: int, **params):
        method = 'photos.get'
        default_params = {
            'extended': 1,
            'owner_id': user_id,
            **params
        }
        content = self.api.get(method, **default_params).json()

        if 'error' in content:
            raise ValueError(f'Некорретные данные запроса фотографии: {content["error"]}')

        return content


if __name__ == "__main__":
    vk = ApiVK()
    params = {
        'album_id': 'profile',
    }
    extractor = ExtractorVK(vk)
    print(extractor.get_photos(552934290, **params))
