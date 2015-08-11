from mysql.connector import (connection)
import telebot
from string import Template
import sys

TG_TOKEN = ''
TG_CHATID = ''
MYSQL_USER = ''
MYSQL_PASS = ''
MYSQL_HOST = ''
query = """
select user, email from users;
"""
template_string = "$user <$email>"



cnx = connection.MySQLConnection(user=MYSQL_USER, password=MYSQL_PASS,
                                 host=MYSQL_HOST)
tb = telebot.TeleBot(TG_TOKEN)
cursor = cnx.cursor(dictionary=True)
cursor.execute(query)

for row in cursor:
	try:
		tb.send_message(TG_CHATID,Template(template_string).safe_substitute(row))
	except telebot.apihelper.ApiException,e:
		print e.result.data
cursor.close()
cnx.close()
