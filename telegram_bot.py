import telebot
import random
import os
import time
import argparse
from dotenv import load_dotenv, find_dotenv
from apod import apod

bot = telebot.TeleBot(token='6557313479:AAG3rsv6DzLNigHmHKDN-MCVcJRxdimdMxo')
updates = bot.get_updates()
parser = argparse.ArgumentParser(description='устанавливает нужный период отправки фото')
parser.add_argument('--count', type=int, help='Ссылка на запуск')
args = parser.parse_args()

dir = 'pictures'
number = []
pictdir = []
for docs in os.walk(dir):
    pictdir.append(docs[2])
    for i_number, i in enumerate(pictdir[0]):
        number.append(i_number)
while True:
        list_random_foto = random.sample(pictdir[0], max(number))
        print(list_random_foto)
        for pic in list_random_foto:
            bot.send_document(chat_id='@cosmopics', document=open(('pictures/'+pic), 'rb'))
            if args.count:
                time.sleep(args.count)
            else:
                time.sleep(14400)


# print(type(timer))
