import telebot
from telebot import types

from m_token import bot

from m_listener import listener, reg_arch

from comandos.m_kyu import command_kyu

mi_id = ##

bot.set_update_listener(listener)		

@bot.message_handler(commands=["registro"])		
def command_registro(m):	
	cid = m.chat.id
	if cid != mi_id:
		return 
	bot.send_document(cid,open(reg_arch,"rb"))

@bot.message_handler(commands=["soporte"])		
def command_soporte(m):	
	cid = m.chat.id
	if len(m.text.split()) == 1:
		bot.send_message(cid, "Para contactar con el creador usa '/soporte tu mensaje'")
	else:
		bot.send_message(mi_id, str(cid) + "," + m.chat.first_name + ":" + m.text)
		bot.send_message(cid, "Gracias!")

@bot.message_handler(commands=["rsoporte"])		
def command_rsoporte(m):	
	cid = m.chat.id
	if cid != mi_id:
		return 
	mt = m.text.split()
	bot.send_message(mt[1]," ".join(mt[2:]))

bot.polling(none_stop=True)