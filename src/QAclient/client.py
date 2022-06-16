import requests
from apiclient import endpoint


@endpoint(base_url='https://qanswer-core1.univ-st-etienne.fr/api/')
class Endpoint:
    login = 'user/signin'
    upload = 'dataset/upload'
    index = 'dataset/index'
    remove = 'dataset/remove'
    update = 'dataset/edit'


class QAClient:
    def __init__(self):
        self.token = None

    def login(self, username, password):
        json_data = {
            'usernameOrEmail': username,
            'password': password
        }
        response = requests.post(Endpoint.login, json=json_data)
        self.token = response.json().get('accessToken', None)

    def new_dataset(self, set_name: str, dataset: str) -> int:
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        params = {
            'dataset': set_name
        }

        files = {
            'file': (f'{set_name}.nt', dataset)
        }

        response = requests.post(Endpoint.upload, params=params, headers=headers, files=files)

        self.index_dataset(set_name)

        return response.status_code

    def index_dataset(self, set_name: str) -> int:
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        json_data = {
            'dataset': f'{set_name}'
        }

        response = requests.post(Endpoint.index, headers=headers, json=json_data)

        return response.status_code

    def remove_dataset(self, set_name: str) -> int:
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        params = {
            'dataset': f'{set_name}'
        }

        response = requests.post(Endpoint.remove, headers=headers, params=params)

        return response.status_code

    def update_dataset(self, set_name: str, file_loc: str) -> int:
        pass
