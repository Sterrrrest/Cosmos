import telebot

bot = telebot.TeleBot(token='6557313479:AAG3rsv6DzLNigHmHKDN-MCVcJRxdimdMxo')
# print(bot.get_me())

bot.send_message(chat_id='@cosmopics', text="I'm sorry Dave I'm afraid I can't do that.")