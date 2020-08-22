import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self):
        file_path = input('Введите полный путь до файла (например С:/folder/.../file.txt): ')
        headers = {'Authorization': f'OAuth {self.token}'}
        file_name = file_path.split('/')[::-1][0]
        path_to = 'disk:/' + file_name
        params = {'path': path_to}

        response_get = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers, params=params)
        upload_link = response_get.json()['href']

        with open(file_path, 'rb') as f:
            files = {'file': f}
            response_put = requests.put(upload_link, headers=headers, files=files)

        print('Файл успешно загружен!')


uploader = YaUploader(input('Пожалуйста, введите свой токен: '))
uploader.upload()