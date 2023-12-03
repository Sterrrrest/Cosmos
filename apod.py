import json
import argparse
import requests
import os

from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse
from pathlib import Path
from os.path import join
from get_extention import get_ext
from download_picture import download_picture


def apod(url, token):
  payLoad = {'api_key': token,
             'count': '3'}
  response = requests.get(url, params=payLoad)
  response.raise_for_status()
  for pic_number, pic in enumerate(response.json()):
    pic_name = pic['url']
    download_picture('pictures_nasa/nasa_{}{}'.format(pic_number,get_ext(pic['url'])), pic_name)
    print("File saved as nasa_{}{}".format(pic_number, get_ext(pic['url'])))

if __name__ == '__main__':
  Path("pictures_nasa").mkdir(parents=True, exist_ok=True)
  load_dotenv(find_dotenv())
  token = os.environ['NASA_TOKEN']
  parser = argparse.ArgumentParser(description='Скачиввает фото Картинки дня NASA по id, '
                                               'если id нет, то фото послднеего фото')
  parser.add_argument('-l', '--link', help='Ссылка на запуск')
  args = parser.parse_args()
  if not args.link:
    apod('https://api.nasa.gov/planetary/apod', token)
  else:
    apod(args.link, token)