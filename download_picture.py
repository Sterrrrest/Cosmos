import requests

def download_picture(filename, url):
  response = requests.get(url)
  response.raise_for_status()
  with open(filename, 'wb') as file:
      file.write(response.content)