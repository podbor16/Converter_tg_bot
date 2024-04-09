"""Программа для записи номеров телефонов с именами владельцев и хэшированием их через Redis.
Ввод данных производится через input(). Вывод данных производится через print()."""

import redis
import json


red = redis.Redis(
	host='redis-16744.c281.us-east-1-2.ec2.cloud.redislabs.com',
	port=16744,
	password='yMQSMv393zMfQq0y0ndsndlNPEv1UGxA'
)

while True:
	print("Доступные команды:\n1. write\n2. read\n3. delete\n4. exit/quit/stop")
	action = input("Введите команду: ").lower()
	if action == "write" or action == '1':
		name = input("Введите имя: ")
		phone = input("Введите телефон: ")
		phone_hash = red.set(name, phone)
	elif action == "read" or action == '2':
		name = input("Введите имя для поиска: ")
		phone = red.get(name)
		if phone:
			print(f"Телефон пользователя '{name}': {phone}")
		else:
			print(f"Телефон для пользователя '{name}' не найден")
	elif action == "delete" or action == '3':
		name = input("Введите имя для удаления: ")
		phone = red.delete(name)
		if phone:
			print(f"Телефон пользователя '{name}' удален")
		else:
			print(f"Телефон пользователя '{name}' не найден")
	elif action == "exit" or action == "quit" or action == "stop":
		break
	else:
		print("Не знаю такой команды, повторите ввод!")


