from api import ApiOK


class ExtractorOK:
    def __init__(self, api):
        if not isinstance(api, ApiOK):
            raise NotImplemented
        self.api = api

    def get_photos(self, user_id: int, **params):
        method = 'photos.getPhotos'
        fields = ['PIC_MAX', 'LIKE_COUNT', 'CREATED_MS', 'STANDARD_HEIGHT', 'STANDARD_WIDTH']
        default_params = {
            'fid': user_id,
            'fields': ','.join([f'photo.{field}' for field in fields]),
            **params
        }

        content = self.api.get(method, **default_params).json()
        if 'error_msg' in content:
            raise ValueError(f'Некорретные данные запроса фотографии: {content["error_msg"]}')
        return content


if __name__ == "__main__":
    try:
        import mytoken
        ok = ApiOK(mytoken.ok['access_token'], mytoken.ok['secret_key'], mytoken.ok['app_key'])
        extractor = ExtractorOK(ok)
        content = extractor.get_photos(576783256198)
        print(content)
    except ImportError:
        pass
