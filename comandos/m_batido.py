from random import choice, randint
from m_token import bot
from bs4 import BeautifulSoup
from mod.leerweb import leerweb

web = "https://www.gettyimages.es/fotos/batido-bebida?mediatype=photography&page="
props = "&phrase=milkshake&sort=mostpopular"

@bot.message_handler(commands=["batido"])		
def command_batido(m):
	for _ in range(3):
		try:
			print('trying batido...')
			cid = m.chat.id
			body = BeautifulSoup(leerweb(f"{web}{randint(1,100)}{props}"),"lxml")
			images = body.find_all("article")
			bot.send_photo(cid, choice(images).find('img')["src"])
		except:
			pass
		else:
			break