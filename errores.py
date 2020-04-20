import telebot
from telebot import types
from m_token import bot as ca, mi_id

def error(error, lugar):
	ca.send_message(mi_id, "Error: " + str(error) + ":::" + str(lugar))