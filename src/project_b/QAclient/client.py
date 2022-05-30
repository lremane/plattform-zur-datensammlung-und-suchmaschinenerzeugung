import requests
import config
from apiclient import endpoint


@endpoint(base_url=config.url)
class Endpoint:
    login = 'user/signin'
    upload = 'dataset/upload'
    index = 'dataset/index'
    remove = 'dataset/remove'
    update = 'dataset/edit'


class QAClient:
    def __init__(self):
        self.token = self.login()

    @staticmethod
    def login():
        json_data = {
            'usernameOrEmail': f'{config.username}',
            'password': f'{config.password}'
        }

        response = requests.post(Endpoint.login, json=json_data)

        return response.json()['accessToken']

    def new_dataset(self, set_name, file_loc):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        params = {
            'dataset': set_name
        }

        files = {
            'file': open(file_loc, 'rb')
        }

        response = requests.post(Endpoint.upload, params=params, headers=headers, files=files)

        self.index_dataset(set_name)

        return response.status_code

    def index_dataset(self, set_name):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        json_data = {
            'dataset': f'{set_name}'
        }

        response = requests.post(Endpoint.index, headers=headers, json=json_data)

        return response.status_code

    def remove_dataset(self, set_name):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        params = {
            'dataset': f'{set_name}'
        }

        response = requests.post(Endpoint.remove, headers=headers, params=params)

        return response.status_code

    def update_dataset(self, set_name, file_loc):
        pass
