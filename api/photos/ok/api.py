import requests
from hashlib import md5


class ApiOK:
    __base_url = 'https://api.ok.ru/fb.do'

    def __init__(self, access_token, secret_key, app_key):
        self.access_token = access_token
        self.secret_key = secret_key
        self.app_key = app_key

    @property
    def default_params(self):
        return {
            'format': 'json',
            'application_key': self.app_key,
        }

    def __base_request_params(self, method: str, additional_params):
        return {
            **self.default_params,
            **additional_params,
            'method': method
        }

    def __get_sig(self, method: str, additional_params):
        params = self.__base_request_params(method, additional_params)
        line = "".join([f'{key}={params[key]}' for key in sorted(params.keys())]) + self.secret_key
        return md5(line.encode('utf-8')).hexdigest().lower()

    def get(self, method: str, **additional_params):
        params = {
            **self.__base_request_params(method, additional_params),
            'access_token': self.access_token,
            'sig': self.__get_sig(method, additional_params),
        }

        response = requests.get(f'{ApiOK.__base_url}', params)
        if response.status_code != 200:
            raise ValueError(f'Не смог получить данные: код ответа{response.status_code}')
        return response


if __name__ == "__main__":
    try:
        import mytoken

        ok = ApiOK(mytoken.ok['access_token'], mytoken.ok['secret_key'], mytoken.ok['app_key'])
        params = {'fid': 576783256198}
        response = ok.get('photos.getPhotos', **params)
        print(response.url)
        print(response.json())
    except ImportError:
        pass
