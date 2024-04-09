import redis
import json


red = redis.Redis(
	host='redis-16744.c281.us-east-1-2.ec2.cloud.redislabs.com',
	port=16744,
	password='yMQSMv393zMfQq0y0ndsndlNPEv1UGxA'
)

"""dict1 = {'key1': 'value1', 'key2': 'value2'}
# С помощью dumps() мы можем преобразовать словарь в строку
red.set('dict1', json.dumps(dict1))

# С помощью loads() мы можем преобразовать данные из кэша обратно в словарь
converted_dict = json.loads(red.get('dict1'))
print(type(converted_dict))
print(converted_dict)
print(type(dict1))
print(dict1)
"""
print(red.get('key'))
print(red.get('dict1'))
red.delete('dict1')
print(red.get('dict1'))