from sys import argv
from requests import get

import telebot

try:
    token = argv[1]
except IndexError:
    print('Usage: python main.py 5396450834:AAEoOmv6JiLpeBaBzbi8pVz8dszITYnhTSU')
    exit(1)
bot_token=os.environ.get("BOT_TOKEN"),

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Send /ip <IP address> and get its location')

@bot.message_handler(commands=['ip'])
def ip(message):
    ip = message.text
    ip = ip[4:]
    json = get('http://ipwhois.app/json/' + ip).json()
    print(json)
    if json['success'] == True and not ip == '127.0.0.1':
        bot.send_message(message.from_user.id, 'IP: ' + json['ip'] + '\nLocation: ' + json['city'] + ', ' + json['region'] + ', ' + json['country'] + '\nTimezone: ' + json['timezone_name'])
    else:
        bot.send_message(message.from_user.id, 'Error')
        
        

bot.infinity_polling()
