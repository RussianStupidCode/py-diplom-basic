import requests

DEFAULT_VK_TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
DEFAULT_VK_API_VERSION = 5.131


class ApiVK:
    __base_url = 'https://api.vk.com/method/'

    def __init__(self, token=DEFAULT_VK_TOKEN, api_version=DEFAULT_VK_API_VERSION):
        self.token = token
        self.api_version = api_version

    @property
    def default_params(self):
        return {
            'v': self.api_version,
            'access_token': self.token
        }

    def get(self, method: str, **additional_params):
        params = {**self.default_params, **additional_params}
        response = requests.get(f'{ApiVK.__base_url}{method}', params)
        if response.status_code != 200:
            raise ValueError(f'Не смог получить данные: код ответа{response.status_code}')
        return response


if __name__ == "__main__":
    vk = ApiVK()
    method = 'photos.get'
    params = {
        'owner_id': 552934290,
        'album_id': 'profile',
        'extended': 1,
    }

    response = vk.get(method, **params)
    text = response.json()
    print(text)
