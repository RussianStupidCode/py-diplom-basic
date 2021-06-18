import requests


class YaUploader:
    __base_url = 'https://cloud-api.yandex.net/v1/disk'
    __prefix = 'disk:'

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}

    def __get_url_for_load(self, file_name: str):
        """Получение адреса для загрузки файла"""

        params = {'path': file_name}
        resp = requests.get(f'{YaUploader.__base_url}/resources/upload', headers=self.headers, params=params)

        text = resp.json()
        if resp.status_code != 200:
            raise ValueError(text['message'])

        return text['href']

    def make_directory(self, dir_path):
        dir_path = dir_path.strip().strip("/")
        params = {'path': dir_path}
        resp = requests.put(f'{YaUploader.__base_url}/resources', headers=self.headers, params=params)

        text = resp.json()
        if resp.status_code != 201 and "уже существует" not in text['message']:
            raise ValueError(text['message'])
        return 'Директория создана успешно'

    def is_valid_token(self):
        resp = requests.get(f'{YaUploader.__base_url}/', headers=self.headers)
        if resp.status_code != 200:
            return False
        return True

    def upload(self, file_name, file_content, ya_dir_path=""):
        normalize_path = ya_dir_path.strip().strip("/")
        ya_dir_path = f'{normalize_path}/{file_name}'

        try:
            href = self.__get_url_for_load(ya_dir_path)
            resp = requests.put(href, headers=self.headers, data=file_content)
        except ValueError as error:
            return error

        if resp.status_code != 201:
            text = resp.json()
            return text['message']
        return 'Файл создан успешно'

    def disk_info(self):
        resp = requests.get(f'{YaUploader.__base_url}/', headers=self.headers)
        if resp.status_code != 200:
            raise ValueError(f'ошибка при ответе: {resp.status_code}')
        return resp.json()
