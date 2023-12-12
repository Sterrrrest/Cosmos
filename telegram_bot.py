import telebot
import random
import os
import time
import argparse

from dotenv import load_dotenv, find_dotenv

if __name__ == '__main__':
        load_dotenv(find_dotenv())
        token = os.environ['TG_TOKEN']
        chat_id = os.environ['CHAT_ID']
        bot = telebot.TeleBot(token=token)
        parser = argparse.ArgumentParser(description='Отправляет скаченные фото в ТГ бота.'
                                                     'В качестве аргумента надо задать период отправки')
        parser.add_argument('--count', type=int, required=False, default=4, help='Укажите ID запуск')
        args = parser.parse_args()

        dir = 'pictures'
        picture_numbers = []
        all_pictures = []
        for docs in os.walk(dir):
            all_pictures.append(docs[2])
        while True:
            random_foto = random.choice(all_pictures[0])
            with open(('pictures/' + random_foto), 'rb') as picture:
                bot.send_document(chat_id=chat_id, document=picture)
            time.sleep(args.count)