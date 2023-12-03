import json
import argparse
import requests
import os

from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse
from pathlib import Path
from os.path import join
from download_picture import download_picture

Path("pictures").mkdir(parents=True, exist_ok=True)

def fetch_spacex_last_launch(url):
  # url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
  response = requests.get(url)
  response.raise_for_status()
  pictures = response.json()["links"]['flickr']['original']
  for picture_number, picture in enumerate(pictures):
    download_picture('pictures/spacex_{}.jpeg'.format(picture_number), picture)
    print("File saved as spacex_{}.jpeg".format(picture_number))

if __name__ == '__main__':
  load_dotenv(find_dotenv())
  token = os.environ['NASA_TOKEN']
  parser = argparse.ArgumentParser(description='Скачиввает фото с запусков space_X_images по id, '
                                               'если id нет, то фото послднего запуска')
  parser.add_argument('-l', '--link', help='Ссылка на запуск')
  args = parser.parse_args()
  # print(args.link)
  if not args.link:
    fetch_spacex_last_launch('https://api.spacexdata.com/v5/launches/5eb87ce3ffd86e000604b336')
  else:
    fetch_spacex_last_launch(args.link)
