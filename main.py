import requests
import os

my_token = "AQAAAAAnK65CAADLW49TAXPXR0YRvGe14ErHUgc"
my_list = ['/Users/rup/Work/BTC/Shit/Contact-57369037-attachment-305508360.png',
           '/Users/rup/Work/BTC/profilowej-ikony-avatar-mężczyzna-modnisia-stylu-męska-moda-62449823.jpg',
           '/Users/rup/Work/BTC/Proxy boto.txt']

class Ya_Disk:

    def __init__(self,token,file_path_list):
        self.token = token
        self.file_path_list = file_path_list

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

    def _get_upload_link(self,file_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path":file_name, "overwrite":'true'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload_files(self):
        added_files = []
        for file in self.file_path_list:
            yandex_file_path = os.path.basename(file)
            href = self._get_upload_link(yandex_file_path).get('href','')
            response = requests.put(href, data=open(file, 'rb'))
            if response.status_code == 201:
                added_files += [yandex_file_path]
        return print(f'Файлы {", ".join(added_files)} успешно загружены на ЯДиск')


yandex = Ya_Disk(my_token,my_list)

yandex.upload_files()
