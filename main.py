import telebot
import requests
import json
import InlineKeyboardMarkup 
import InlineKeyboardButton
import random
import os

bot = telebot.TeleBot('5380148604:AAH5Qi5lgzQj8yufhGfS0oYxKpVANhOlJew')



TEXT = """**Hola {},
Con este bot podras geolocalizar cualquier ip**
Solo escribe la ip y listo"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Soporte ⭕️", url = "https://t.me/lord_zeper")
        ],
        
    ]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

@bot.message_handler(func=lambda message: True)
def IP(message):
	url = f'https://api.freegeoip.app/json/{message.text}?apikey=a9c7ad60-4b8e-11ec-bf1d-e384c4f2ace1'
	result = requests.get(url).content
	parse_json = json.loads(result)
	bot.reply_to(message, f'----------------------------------------------- \n                    IP Detail\n----------------------------------------------- \nIP: {parse_json["ip"]} \nCountry Code: {parse_json["country_code"]} \nCountry Name: {parse_json["country_name"]} \nRegion Code: {parse_json["region_code"]} \nRegion Name: {parse_json["region_name"]} \nCity: {parse_json["city"]} \nZip Code: {parse_json["zip_code"]} \nTime Zone: {parse_json["time_zone"]} \nLatitude: {parse_json["latitude"]} \nLongitude: {parse_json["longitude"]} \nMetro Code: {parse_json["metro_code"]}')

bot.polling()
