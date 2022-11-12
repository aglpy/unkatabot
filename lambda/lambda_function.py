import telebot
from telebot import types
from m_token import bot, mi_id, group_id
from random import choice
from bs4 import BeautifulSoup
import urllib.request
from threading import Thread
import sys
import time
import datetime
	
def leerweb(pag):
	try:
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
		req = urllib.request.Request(pag, headers = headers)
		return urllib.request.urlopen(req)
	except:
		return "Error en leerweb"

def main():
    wd = datetime.datetime.today().weekday()
    codewars = "https://www.codewars.com"
    search = "/kata/search/"
    level_ref = "?q=&r[]=-"
    cat_ref = "&tags="
    opts = "&beta=false&order_by=popularity+desc"
    kata_class = "list-item-kata bg-ui-section p-4 rounded-lg shadow-md"
    level = abs(int(wd/2)-7)
    parser = 'html.parser'

    body = BeautifulSoup(leerweb(f"{codewars}{search}{level_ref}{level}{opts}"),parser)
    cats = [cat.find("a")["href"] for cat in body.find_all(attrs={"class":"py-1"})] # all categories
    cat = choice(cats).split('=')[-1]
    body = BeautifulSoup(leerweb(f"{codewars}{search}{level_ref}{level}{cat_ref}{cat}{opts}"),parser)
    katas = [kata.find("a")["href"] for kata in body.find_all(attrs={"class": kata_class})]
    mensaje = f"{codewars}{choice(katas)}"
    bot.send_message(group_id, mensaje)

    bot.polling()

def lambda_handler(a,b):
    main_thread = Thread(target=main)
    main_thread.daemon = True
    main_thread.start()
    time.sleep(10)
    sys.exit()
