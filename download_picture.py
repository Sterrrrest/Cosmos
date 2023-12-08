import requests

def download_picture(filename, url, token):
    payLoad = {'api_key': token}
    response = requests.get(url, params=payLoad)
    response.raise_for_status()
    with open(filename, 'wb') as file:
      file.write(response.content)