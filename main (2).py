import json
from os.path import join
import requests
import os
from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse
from pathlib import Path

Path("pictures").mkdir(parents=True, exist_ok=True)
Path("pictures_nasa").mkdir(parents=True, exist_ok=True)
Path("pictures_nasa_earth").mkdir(parents=True, exist_ok=True)

def download_picture(filename, url):
  response = requests.get(url)
  response.raise_for_status()
  with open(filename, 'wb') as file:
      file.write(response.content)


def fetch_spacex_last_launch(url):
  url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
  response = requests.get(url)
  response.raise_for_status()
  pictures = response.json()["links"]['flickr']['original']
  for picture_number, picture in enumerate(pictures):
    download_picture('pictures/spacex_{}.jpeg'.format(picture_number), picture)
    print("File saved as spacex_{}.jpeg".format(picture_number))


def get_ext(url):
  path = urlparse(url).path
  ext = os.path.splitext(path)[1]
  return ext


def apod(url, token):
  url = 'https://api.nasa.gov/planetary/apod'
  payLoad = {'api_key': token,
    'start_date': '2023-11-27'}
  response = requests.get(url, params=payLoad)
  response.raise_for_status()
  for pic_number, pic in enumerate(response.json()):
    pic_name = pic['url']
    download_picture('pictures_nasa/nasa_{}{}'.format(pic_number,get_ext(pic['url'])), pic_name)
    print("File saved as nasa_{}{}".format(pic_number, get_ext(pic['url'])))


def nasa_earth(url, token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payLoad = {'api_key': token}
    r = requests.get(url, params=payLoad)
    r.raise_for_status()
    for pic_number, pic in enumerate(r.json()):
      pic_name = pic['image']
      pic_date = pic['date'].split(' ')[0].replace('-', '/')
      url_earth = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(pic_date, pic_name)
      response = requests.get(url_earth, params=payLoad)
      response.raise_for_status()
      download_picture('pictures_nasa_earth/earth_{}.png'.format(pic_number), response.url)
      print("File saved as earth_{}.png".format(pic_number))

if __name__ == '__main__':
  load_dotenv(find_dotenv())
  print(os.environ['NASA_TOKEN'])
  token = os.environ['NASA_TOKEN']

  nasa_earth('https://api.nasa.gov/EPIC/api/natural', token)
  apod('https://api.nasa.gov/planetary/apod', token)
  fetch_spacex_last_launch('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')