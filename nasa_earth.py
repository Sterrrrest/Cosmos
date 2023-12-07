import argparse
import requests
import os


from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from download_picture import download_picture


def nasa_earth(foto_id, token):
    payLoad = {'api_key': token}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural' + foto_id, params=payLoad)
    response.raise_for_status()
    for pic_number, pic in enumerate(response.json()):
      pic_name = pic['image']
      pic_date = pic['date'].split(' ')[0].replace('-', '/')
      url_earth = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(pic_date, pic_name)
      response = requests.get(url_earth, params=payLoad)
      response.raise_for_status()
      download_picture('pictures_nasa_earth/earth_{}.png'.format(pic_number), response.url)
      print("File saved as earth_{}.png".format(pic_number))

if __name__ == '__main__':
  Path("pictures_nasa_earth").mkdir(parents=True, exist_ok=True)
  load_dotenv(find_dotenv())
  token = os.environ['NASA_TOKEN']
  parser = argparse.ArgumentParser(description='Скачивает фото Земли')
  parser.add_argument('-l', '--x', help='Id фото')
  args = parser.parse_args()
  if not args.link:
    nasa_earth('https://api.nasa.gov/EPIC/api/natural', token)
  else:
    nasa_earth(args.x, token)