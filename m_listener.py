import telebot
from telebot import types
from m_token import bot

reg_arch = "./datos/registro.txt"

def listener(messages):
	try:
		for m in messages:
			cid = m.chat.id
			if cid > 0:
				mensaje = str(m.chat.first_name) + "(" + str(cid) + ")" + str(m.text)
			else:
				uid = m.from_user.id
				mensaje = str(m.chat.first_name).encode("utf-8") + "-" + str(m.from_user.first_name).encode("utf-8") 
				mensaje += "(" + str(cid) + "*" + str(uid) + ")" + str(m.text).encode("utf-8")
			with open(reg_arch,"a") as arch:
				arch.write(mensaje + "\n")	
			print(mensaje)					
	except:
		pass