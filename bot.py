# -*- coding: utf-8 -*-
# Codigo para MyBot
import telebot
from telebot import types
from importlib import reload

#Importamos el bot definido por el token en m_token 
from m_token import bot, mi_id

#Importamos el modulo listener
from m_listener import listener, reg_arch

#Importamos los modulos de los comandos
from comandos.m_kyu import command_kyu
from comandos.m_almuerzo import command_almuerzo
from comandos.m_batido import command_batido


#Asociamos la funcion listener a la propiedad que escucha los mensajes
bot.set_update_listener(listener)		

#Actualiza los modulos
@bot.message_handler(commands=["update"])
def command_update(m):	
	cid = m.chat.id
	if cid != mi_id:
		return 
	#Crear un actualizador de modulos con reload, no funciona con import . from .
	
#Cierra el bot	
@bot.message_handler(commands=["exit"])
def command_exit(m):	
	cid = m.chat.id
	if cid != mi_id:
		return 
	bot.polling(none_stop=False)

#Manda el registro
@bot.message_handler(commands=["registro"])		
def command_registro(m):	
	cid = m.chat.id
	if cid != mi_id:
		return 
	bot.send_document(cid,open(reg_arch,"rb"))

#Manda una peticion de soporte
@bot.message_handler(commands=["soporte"])		
def command_soporte(m):	
	cid = m.chat.id
	if len(m.text.split()) == 1:
		bot.send_message(cid, "Para contactar con el creador usa '/soporte tu mensaje'")
	else:
		bot.send_message(mi_id, str(cid) + "," + m.chat.first_name + ":" + m.text)
		bot.send_message(cid, "Thanks!")

#Responde a la peticion de soporte
@bot.message_handler(commands=["rsoporte"])		
def command_rsoporte(m):	
	cid = m.chat.id
	if cid != mi_id:
		return 
	mt = m.text.split()
	bot.send_message(mt[1]," ".join(mt[2:]))
	
#Hacemos que el bot nunca se pare
bot.polling(none_stop=True)