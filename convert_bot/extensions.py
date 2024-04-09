import requests
import json
from config import keys


class APIException(Exception):
	pass


class Converter:
	@staticmethod
	def get_price(quote: str, base: str, amount: str):

		# вызов исключения, если пользователь пытается конвертировать валюту в саму себя
		if quote == base:
			raise APIException(f"Нельзя перевести валюту '{base}' в нее же!")

		# инициализируем новые переменные, которые будут хранить значения словаря keys
		quote_ticker, base_ticker = keys[quote], keys[base]

		try:
			quote_ticker = keys[quote]
		except KeyError:
			raise APIException(f"Не удалось обработать валюту'{quote}'")

		try:
			base_ticker = keys[base]
		except KeyError:
			raise APIException(f"Не удалось обработать валюту'{base}'")

		try:
			amount = float(amount)
		except ValueError:
			raise APIException(f"Не удалось обработать количество валюты '{amount}'")

		# далем GET-запрос к API cryptocompare.com, который конвертирует одну валюту в другую
		# обращаемся к словарю по индексам quote и base
		r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
		total_base = json.loads(r.content)[keys[base]]

		return total_base * amount
