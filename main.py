import json
import argparse
import requests
import os

from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse
from pathlib import Path
from os.path import join

Path("pictures").mkdir(parents=True, exist_ok=True)
Path("pictures_nasa").mkdir(parents=True, exist_ok=True)
Path("pictures_nasa_earth").mkdir(parents=True, exist_ok=True)


def fetch_spacex_last_launch(url):
  url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
  response = requests.get(url)
  response.raise_for_status()
  pictures = response.json()["links"]['flickr']['original']
  for picture_number, picture in enumerate(pictures):
    download_picture('pictures/spacex_{}.jpeg'.format(picture_number), picture)
    print("File saved as spacex_{}.jpeg".format(picture_number))


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




if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Скачиввает фото с запусков space_X_images')
  parser.add_argument('link', help='Ссылка на запуск')
  args = parser.parse_args()
  link = args.link
  load_dotenv(find_dotenv())
  token = os.environ['NASA_TOKEN']

  # nasa_earth('https://api.nasa.gov/EPIC/api/natural', token)
  # apod('https://api.nasa.gov/planetary/apod', token)
  fetch_spacex_last_launch(args.link)