import telebot
import requests
import json

bot = telebot.TeleBot('BOT_TOKEN')

@bot.message_handler(commands=['start'])
def greet(message):
	bot.reply_to(message, f'Welcome, Please enter a valid IP address to get the detail')


@bot.message_handler(func=lambda message: True)
def IP(message):
	url = f'https://api.freegeoip.app/json/{message.text}?apikey=a9c7ad60-4b8e-11ec-bf1d-e384c4f2ace1'
	result = requests.get(url).content
	parse_json = json.loads(result)
	bot.reply_to(message, f'----------------------------------------------- \n                    IP Detail\n----------------------------------------------- \nIP: {parse_json["ip"]} \nCountry Code: {parse_json["country_code"]} \nCountry Name: {parse_json["country_name"]} \nRegion Code: {parse_json["region_code"]} \nRegion Name: {parse_json["region_name"]} \nCity: {parse_json["city"]} \nZip Code: {parse_json["zip_code"]} \nTime Zone: {parse_json["time_zone"]} \nLatitude: {parse_json["latitude"]} \nLongitude: {parse_json["longitude"]} \nMetro Code: {parse_json["metro_code"]}')

bot.polling()
