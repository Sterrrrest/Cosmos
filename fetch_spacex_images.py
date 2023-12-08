import argparse
import requests


from pathlib import Path
from download_picture import download_picture

def fetch_spacex_last_launch(launch_id):
    response = requests.get('https://api.spacexdata.com/v5/launches/'+ launch_id)
    response.raise_for_status()
    pictures = response.json()["links"]['flickr']['original']
    for picture_number, picture in enumerate(pictures):
        download_picture('pictures/spacex_{}.jpeg'.format(picture_number), picture, token=0)
        print("File saved as spacex_{}.jpeg".format(picture_number))

if __name__ == '__main__':
    Path("pictures").mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(description='Скачиввает фото с запусков space_X_images по id, '
                                                 'если id нет, то фото послднего запуска')
    parser.add_argument('--x', required=False, default='latest', help='Id запуска')
    args = parser.parse_args()
    args.x = '5eb87d47ffd86e000604b38a'
    fetch_spacex_last_launch(args.x)
