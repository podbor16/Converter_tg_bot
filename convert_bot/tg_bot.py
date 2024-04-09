"""Телеграмм-бот, который конвертирует одну валюту в другую"""

import telebot
from config import TOKEN, keys
from extensions import APIException, Converter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help_message(message: telebot.types.Message):
	"""Обработчик команд /start и /help"""
	text = ("Чтобы начать работу, введите команду боту в следующем формате:\n<валюта>\
<в какую валюту перевести>\
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values")
	# Ответ на сообщение пользователя с командой /help или /start
	bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
	"""Обработчик команды /values, который выводит список всех доступных валют"""
	text = "Доступные валюты:"
	# Проходимся по ключам из словаря keys, который содержит все доступные валюты
	for key in keys.keys():
		# к новой строке присоединяем ключ из словаря keys (валюта)
		text = '\n'.join((text, key))
	# Ответ на сообщение пользователя с командой /values
	bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
	"""Основной обработчик, который конвертирует одну валюту в другую"""
	try:
		values_ = message.text.lower().split(' ')
		# вызов исключения, если количество аргументов больше 3
		if len(values_) != 3:
			raise APIException("Неверное количество параметров")
		# quote - валюта, которую нужно конвертировать
		# base - валюта, в которую нужно конвертировать
		# amount - количество валюты quote, которую нужно конвертировать
		quote, base, amount = values_
		total_base = Converter.get_price(quote, base, amount)
	except APIException as e:
		bot.reply_to(message, f'Ошибка пользователя.\n{e}')
	except Exception as e:
		# Если возникло исключение, то отправляем сообщение с ошибкой
		bot.reply_to(message, f"Не удалось обработать команду\n{e}")
	else:
		text = f"Цена {amount} {quote} в {base}: {total_base}"
		bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
