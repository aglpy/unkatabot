from random import choice, randint
from m_token import bot
from bs4 import BeautifulSoup
from mod.leerweb import leerweb

web = "https://www.foodiesfeed.com/trending-photos/page/"

@bot.message_handler(commands=["almuerzo"])		
def command_almuerzo(m):
	try:
		cid = m.chat.id
		body = BeautifulSoup(leerweb(f"{web}{randint(1,43)}/"),"lxml")
		images = body.find_all(attrs={"class":"post-item item"})	
		bot.send_photo(cid, choice(images).find("img")["src"])
	except:
		pass
