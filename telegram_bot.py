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
        updates = bot.get_updates()
        parser = argparse.ArgumentParser(description='Отправляет скаченные фото в ТГ бота.'
                                                     'В качестве аргумента надо задать период отправки')
        parser.add_argument('--count', type=int, required=False, default=14400, help='Ссылка на запуск')
        args = parser.parse_args()

        dir = 'pictures'
        number = []
        pictdir = []
        for docs in os.walk(dir):
            pictdir.append(docs[2])
            for directory_path_number, directory_path in enumerate(pictdir[0]):
                number.append(directory_path_number)
        while True:
            random_foto = random.sample(pictdir[0], max(number))

            for pic in random_foto:
                with open(('pictures/' + pic), 'rb') as picture:
                    bot.send_document(chat_id=chat_id, document=picture)
                    time.sleep(args.count)
