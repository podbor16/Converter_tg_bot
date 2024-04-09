import requests
import json

data = {'key': 'value'}
# Отправляем пост-запрос
r = requests.post('https://httpbin.org/post')
# отправляем пост-запрос с типом данных JSON
json = json.dumps(data)
# Содержимое ответа и его обработка происходит так же, как и с ГЕТ-запросами, разницы никакой нет
print(r.content)

"""
r = requests.get('https://api.github.com')
# Делает из полученных байтов python-объект для удобной работы
d = json.loads(r.content)
print(type(d))
# Обращаемся к полученному объекту как к словарю и пробуем напечатать его значение
print(d['following_url'])"""

"""
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# Делает из полученных байтов python-объект для удобной работы
texts = json.loads(r.content)
# Проверяем тип
print(type(texts))

# Печать текста по 50 символов в строке
for text in texts:
	print(text[:50], '\n')"""

