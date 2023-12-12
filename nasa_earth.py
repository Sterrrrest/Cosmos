import argparse
import requests
import os


from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from download_picture import download_picture


def nasa_earth(token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payLoad = {'api_key': token}
    response = requests.get(url, params=payLoad)
    response.raise_for_status()
    for pic_number, pic in enumerate(response.json()):
      pic_name = pic['image']
      pic_date = pic['date'].split(' ')[0].replace('-', '/')
      final_url = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(pic_date, pic_name)
      download_picture('pictures_nasa_earth/earth_{}.png'.format(pic_number), final_url, token)
      print("File saved as earth_{}.png".format(pic_number))

if __name__ == '__main__':
  Path("pictures_nasa_earth").mkdir(parents=True, exist_ok=True)
  load_dotenv(find_dotenv())
  token = os.environ['NASA_TOKEN']
  nasa_earth(token)