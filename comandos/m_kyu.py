from random import choice
from m_token import bot
from bs4 import BeautifulSoup
from mod.leerweb import leerweb

codewars = "https://www.codewars.com"
search = "/kata/search/"
level_ref = "?q=&r%5B%5D=-"
opts = "&beta=false&order_by=popularity+desc"

@bot.message_handler(commands=["kyu"])		
def command_kyu(m):
	try:
		cid = m.chat.id
		mensaje = ""
		for i in m.text.split()[1:]:	
			body = BeautifulSoup(leerweb(f"{codewars}{search}{level_ref}{i}{opts}"),"lxml")
			cats = [cat.find("a")["href"] for cat in body.find_all(attrs={"class":"py-5px"})] # all categories
			body = BeautifulSoup(leerweb(f"{codewars}{search}{choice(cats)}"),"lxml")
			katas = [kata.find("a")["href"] for kata in body.find_all(attrs={"class":"list-item kata"})]
			mensaje += f"{i}kyu: {codewars}{choice(katas)}\n\n"
		bot.send_message(cid, mensaje)
	except:
		pass
