import requests
import os


from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from get_extention import get_ext
from download_picture import download_picture


def get_apod(token):
    url = 'https://api.nasa.gov/planetary/apod'
    payLoad = {'api_key': token}
    response = requests.get(url, params=payLoad)
    response.raise_for_status()
    for pic_number, pic in enumerate(response.json()):
      pic_address = pic['url']
      picture_url = "'pictures_nasa/nasa_{}{}'.format(pic_number,get_ext(pic['url'])"
      download_picture(picture_url, pic_address, token)
      print("File saved as nasa_{}{}".format(pic_number, get_ext(pic['url'])))

if __name__ == '__main__':
    Path("pictures_nasa").mkdir(parents=True, exist_ok=True)
    load_dotenv(find_dotenv())
    token = os.environ['NASA_TOKEN']
    get_apod(token)