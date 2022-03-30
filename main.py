import telebot
import requests
from bs4 import BeautifulSoup
import random
from telebot import types
import datetime
from telegram.ext import Updater
API_KEY = ''
bot=telebot.TeleBot(API_KEY)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
itembtn1 = types.KeyboardButton("Cafelutza")
markup.add(itembtn1)
addresses = []
@bot.message_handler(commands=['start'])
def tasta (message):
    bot.send_message(message.chat.id, "Bot-ul de cafelutza este online" , reply_markup=markup)
@bot.message_handler()
def poza (message):
    if(message.text == "Cafelutza"):
        addresses.append(message.chat.id)
        for el in addresses:
            if(el==addresses[addresses.__len__()-1]):
                addresses.pop(addresses.__len__()-1)
                break
        URL = "https://images.search.yahoo.com/search/images;_ylt=AwrhRuU9kjhibnMFBUGJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZANFTEpBc3pFd0xqSkw2TzBwWUoxbXB3RnVPRFl1TVFBQUFBQzFiOHJuBGZyA3NmcARmcjIDc2EtZ3AEZ3ByaWQDa3lSeHpCTkRRbUNuNEw2ZEtoQ1dBQQRuX3N1Z2cDNgRvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDMjkEcXVlcnkDYnVuYSUyMGRpbWluZWF0YSUyMGxhJTIwY2FmZWEEdF9zdG1wAzE2NDc4NzQ2Mzc-?p=buna+dimineata+la+cafea&fr=sfp&fr2=sb-top-images.search&ei=UTF-8&x=wrt"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("img")
        gasit = []
        for line in results:
            if str(line).find("https") != -1 :
                gasit.append(str(line))
        parse1 = gasit[random.randint(0, gasit.__len__() - 1)].split("src")
        link_img = parse1[1].split("\"")
        link_img.remove(link_img[0])
        response = requests.get(url=link_img[0])
        bot.send_photo(message.chat.id, photo=response.content)
bot.infinity_polling()
