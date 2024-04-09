import requests
import lxml.html
from lxml import etree


# Создадим объект ElementTree. Он возвращается функцией parse()
# попытаемся спарсить наш файл с помощью html-парсера.
# Сам html - это то, что мы скачали и поместили в папку из браузера.
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

# Помещаем в аргумент метода findall скопированный xpath. Здесь мы получим все элементы списка новостей.
# (Все заголовки и их даты)
ul = tree.findall('./body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
	# В каждом элементе находим, где хранится заголовок новости.
	# У нас это тег <а>. Т. е. гиперссылка, на которую нужно нажать,
	# чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тег <а>)
	a = li.find('a')
	time = li.find('time')
	print(time.get('datetime'), '\t', a.text)



