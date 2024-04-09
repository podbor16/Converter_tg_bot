import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = '''<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''  # получим html главной странички официального сайта python

tree = lxml.html.document_fromstring(html)
tag = tree.xpath('/html/body/tag1/tag2/text()')  # забираем текст тега <title> из тега <head>, который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

print(tag)  # выводим полученный заголовок страницы