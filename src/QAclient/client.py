import requests
from apiclient import endpoint

# @endpoint(base_url=config.url)
@endpoint(base_url = 'https://qanswer-core1.univ-st-etienne.fr/api/')

class Endpoint:
  login  = 'user/signin'
  upload = 'dataset/upload'
  index  = 'dataset/index'
  remove = 'dataset/remove'
  update = 'dataset/edit'

class QAClient:
  def __init__(self):
    self.token = self.login('', '')

  @staticmethod
  def login(username, password):
    json_data = {
      'usernameOrEmail': username,
      'password':        password
      }

    response = requests.post(Endpoint.login, json = json_data)

    try:
      if not response.json()['accessToken']:
        return '0'
      else:
        return response.json()
    except:
      return '0'

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
