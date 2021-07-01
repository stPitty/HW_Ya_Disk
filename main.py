import requests
import os

my_token = "AQAAAAAnK65CAADLW49TAXPXR0YRvGe14ErHUgc"

class Ya_Disk:

    def __init__(self,token,file_path: str):
        self.token = token
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources/files"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()

    def _get_upload_link(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path":self.file_name, "overwrite":'true'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload_files(self):
        href = self._get_upload_link().get('href','')
        response = requests.put(href, data=open(self.file_path, 'rb'))
        if response.status_code == 201:
            print(f'Файл {self.file_name} успешно загружен на Я.Диск')
        else:
            print('Что-то пошло не так')
            return response.status_code


yandex = Ya_Disk(my_token,'My_Files/example.py')

yandex.upload_files()
