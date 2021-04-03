import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
import random

vk_session = vk_api.VkApi(token = 'e7459baae0b4e3a7b8d92dce2e31cab497368204243caf6b5f7f71a82605f9e7f6188e73ac3427a699bc1') #e7459baae0b4e3a7b8d92dce2e31cab497368204243caf6b5f7f71a82605f9e7f6188e73ac3427a699bc1
longpoll = VkLongPoll(vk_session)
session_api = vk_session.get_api()

class User():
	def __init__(self, msg):
		self.msg = msg
		self.bal = 0
		self.stats = 0
		self.ser = 0
		self.photo = 0
		self.manga = 0

	def tokya(self, event):
		self.event = event
		self.stats = 1

	def list(self, event):
		self.event = event
		self.ser += 1

	def undo(self, event):
		self.event = event
		self.ser -= 1

def sender(id, text):
	vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : random.randint(-12424235, +1245242)})

def photo(id, url):
    vk_session.method('messages.send', {'user_id' : id, 'attachment' : url, 'random_id' : random.randint(-12424235, +1245242)}) 

def get_but(text, color):
	return {
							"action": {
									"type": "text",
									"payload": "{\"button\": \"" + "1" + "\"}",
									"label": f"{text}"
							},
							"color": f"{color}"
					}

anime_key = { 
		'one_time' : True,
		'inline' : False,
		"buttons" : [
				[get_but('Токийский гуль', 'negative')]
		]
}

anime_key = json.dumps(anime_key, ensure_ascii = False).encode('utf-8')
anime_key = str(anime_key.decode('utf-8'))

tokya_key = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Серии', 'positive')],
		[get_but('Фото', 'positive')],
	]
}

tokya_key = json.dumps(tokya_key, ensure_ascii = False).encode('utf-8')
tokya_key = str(tokya_key.decode('utf-8'))

listen_key = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Далее', 'positive')]
	]
}

listen_key = json.dumps(listen_key, ensure_ascii = False).encode('utf-8')
listen_key = str(listen_key.decode('utf-8'))

listen_key2 = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Далее', 'positive')], [get_but('Назад', 'negative')]
	]
}

listen_key2 = json.dumps(listen_key2, ensure_ascii = False).encode('utf-8')
listen_key2 = str(listen_key2.decode('utf-8'))

menu_key = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Аниме', 'positive')],
	]
}

menu_key = json.dumps(menu_key, ensure_ascii = False).encode('utf-8')
menu_key = str(menu_key.decode('utf-8'))


users = {}
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		msg = event.text.lower()
		id = event.user_id
		user_id = session_api.messages.getById(message_ids=event.message_id)['items'][0]['from_id']

		if users.get(user_id) == None:
			users[user_id] = User(msg)

		if msg == 'проверка':
			sender(id, 'Ваше очко: ' + str(users[user_id].photo))

		if msg == 'аниме':
			vk_session.method('messages.send', {'user_id' : id, 'message' : 'Доступные аниме:' + '\n💔Токийский гуль', 'keyboard' : anime_key, 'random_id' : random.randint(-12424235, +1245242)})

		if msg == 'токийский гуль':
			users[user_id].tokya(event)
			if users[user_id].stats == 1:
				vk_session.method('messages.send', {'user_id' : id, 'message' : 'Доступно:' + '\n🎬Серии' + '\n📷Фото (рандомное фото)', 'keyboard' : tokya_key, 'random_id' : random.randint(-12424235, +1245242)})
		
		elif msg == 'серии':
			if users[user_id].stats == 1:
				sender(id, '1 СЕЗОН:' + '\n1 серия - Трагедия - 3 июля 2014' + '\n2 серия - Вылупление - 10 июля 2014 года' + '\n3 серия - Белый голубь - 17 июля - 2014 года' + '\n4 серия - Ужин - 24 июля 2014 года' + '\n5 серия - Шрам - 31 июля 2014 года' + "\n6 серия - Ливень - 7 августа 2014 года")
				vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Пленение - 14 августа 2014 года' + "\n8 серия - Цикл - 21 августа 2014 года" + "\n9 серия - Птичья клетка - 28 августа 2014 года" + "\n10 серия - Аогири - 4 сентября 2014 года" + "\n11 серия - Боевой дух - 11 сентября 2014 года" + '\n12 серия - Гуль - 18 сентября 2014 года', 'keyboard' : listen_key, 'random_id' : random.randint(-12424235, +1245242)})

		if msg == 'далее':
			if users[user_id].stats == 1:
				users[user_id].list(event)
				if users[user_id].ser == 1:
					sender(id, '2 СЕЗОН:' + '\n1 серия - Крах - 9 января 2015 года' + "\n2 серия - Танцующие цветы - 15 января 2015 года" + "\n3 серия - Висельник - 22 января 2015 года" + "\n4 серия - Глубоко внутри - 29 января 2015 года" + "\n5 серия - Раскол - 5 февраля 2015 года" + "\n6 серия - Тысяча путей - 12 февраля 2015 года")
					vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Проникновение - 9 февраля 2015 года' + '\n8 серия - Старая девятка - 26 февраля 2015 года' + '\n9 серия - Затишье в городе - 5 марта 2015 года' + '\n10 серия - Последний дождь - 12 марта 2015 года' + '\n11 серия - Море цветов - 19 марта 2015 года' + '\n12 серия - Кэн - 27 марта 2015 года', 'keyboard' : listen_key2, 'random_id' : random.randint(-12424235, +1245242)})
				if users[user_id].ser == 2:
					sender(id, '3 СЕЗОН:' + '\n1 серия - Те, Кто Охотятся - 3 апреля 2018' + "\n2 серия - Осколки - 10 апреля 2018" + "\n3 серия - Ева - 17 апреля 2018" + "\n4 серия - Аукцион - 24 апреля 2018" + "\n5 серия - Наступающая Ночь - 1 мая 2018" + "\n6 серия - В Конце - 8 мая 2018")
					vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Дни Воспоминаний - 15 мая 2018' + '\n8 серия - Единственный, Кто Страдает - 22 мая 2018' + '\n9 серия - Былой Дух - 29 мая 2018' + '\n10 серия - Встряска - 5 июня 2018' + '\n11 серия - Пропавший без вести - 12 июня 2018' + '\n12 серия - Рассвет - 19 июня 2018', 'keyboard' : listen_key2, 'random_id' : random.randint(-12424235, +1245242)})
				if users[user_id].ser == 3:
					sender(id, '4 СЕЗОН:' + '\n1 серия -  И вновь - 9 октября 2018' + "\n2 серия - Белая тьма - 16 октября 2018" + "\n3 серия - Перекрёстная игра - 23 октября 2018" + "\n4 серия - Сломленный - 30 октября 2018" + "\n5 серия - Встреча с бродягой - 6 ноября 2018" + "\n6 серия - Великолепие - 13 ноября 2018")
					vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Узы - 20 ноября 2018' + '\n8 серия - Пробуждённое дитя - 27 ноября 2018' + '\n9 серия - Напоминание - 4 декабря 2018' + '\n10 серия - Конец трагедии - 11 декабря 2018' + '\n11 серия - Столкновение - 18 декабря 2018' + '\n12 серия - Финал - 25 декабря 2018', 'keyboard' : listen_key2, 'random_id' : random.randint(-12424235, +1245242)})


		if msg == 'назад':
			if users[user_id].stats == 1:
				users[user_id].undo(event)
				if users[user_id].ser == 0:
					sender(id, '1 СЕЗОН:' + '\n1 серия - Трагедия - 3 июля 2014' + '\n2 серия - Вылупление - 10 июля 2014 года' + '\n3 серия - Белый голубь - 17 июля - 2014 года' + '\n4 серия - Ужин - 24 июля 2014 года' + '\n5 серия - Шрам - 31 июля 2014 года' + "\n6 серия - Ливень - 7 августа 2014 года")
					vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Пленение - 14 августа 2014 года' + "\n8 серия - Цикл - 21 августа 2014 года" + "\n9 серия - Птичья клетка - 28 августа 2014 года" + "\n10 серия - Аогири - 4 сентября 2014 года" + "\n11 серия - Боевой дух - 11 сентября 2014 года" + '\n12 серия - Гуль - 18 сентября 2014 года', 'keyboard' : listen_key, 'random_id' : random.randint(-12424235, +1245242)})
				if users[user_id].ser == 1:			
					sender(id, '2 СЕЗОН:' + '\n1 серия - Крах - 9 января 2015 года' + "\n2 серия - Танцующие цветы - 15 января 2015 года" + "\n3 серия - Висельник - 22 января 2015 года" + "\n4 серия - Глубоко внутри - 29 января 2015 года" + "\n5 серия - Раскол - 5 февраля 2015 года" + "\n6 серия - Тысяча путей - 12 февраля 2015 года")
					vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Проникновение - 9 февраля 2015 года' + '\n8 серия - Старая девятка - 26 февраля 2015 года' + '\n9 серия - Затишье в городе - 5 марта 2015 года' + '\n10 серия - Последний дождь - 12 марта 2015 года' + '\n11 серия - Море цветов - 19 марта 2015 года' + '\n12 серия - Кэн - 27 марта 2015 года', 'keyboard' : listen_key2, 'random_id' : random.randint(-12424235, +1245242)})
				if users[user_id].ser == 2:
					sender(id, '3 СЕЗОН:' + '\n1 серия - Те, Кто Охотятся - 3 апреля 2018' + "\n2 серия - Осколки - 10 апреля 2018" + "\n3 серия - Ева - 17 апреля 2018" + "\n4 серия - Аукцион - 24 апреля 2018" + "\n5 серия - Наступающая Ночь - 1 мая 2018" + "\n6 серия - В Конце - 8 мая 2018")
					vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Дни Воспоминаний - 15 мая 2018' + '\n8 серия - Единственный, Кто Страдает - 22 мая 2018' + '\n9 серия - Былой Дух - 29 мая 2018' + '\n10 серия - Встряска - 5 июня 2018' + '\n11 серия - Пропавший без вести - 12 июня 2018' + '\n12 серия - Рассвет - 19 июня 2018', 'keyboard' : listen_key2, 'random_id' : random.randint(-12424235, +1245242)})

		if msg == 'меню':
			vk_session.method('messages.send', {'user_id' : id, 'message' : 'Доступные команды:' + '\n✨Аниме', 'keyboard' : menu_key, 'random_id' : random.randint(-12124142, +14334121)})

		if msg == 'фото':
			if users[user_id].stats == 1:
				users[user_id].photo = random.randint(1, 19)
				if users[user_id].photo == 1:
					photo(id, 'photo-165719265_456239512')
				if users[user_id].photo == 2:
					photo(id, 'photo-134214319_457263539')
				if users[user_id].photo == 3:
					photo(id, 'photo-134214319_457263540')
				if users[user_id].photo == 4:
					photo(id, 'photo-134214319_457263505')
				if users[user_id].photo == 5:
					photo(id, 'photo-134214319_457263425')
				if users[user_id].photo == 6:
					photo(id, 'photo-165719265_456239454')
				if users[user_id].photo == 7:
					photo(id, 'photo-165719265_456239437')
				if users[user_id].photo == 8:
					photo(id, 'photo-165719265_456239428')
				if users[user_id].photo == 9:
					photo(id, 'photo-165719265_456239426')
				if users[user_id].photo == 10:
					photo(id, 'photo-165719265_456239380')
				if users[user_id].photo == 11:
					photo(id, 'photo-186599306_457239284')
				if users[user_id].photo == 12:
					photo(id, 'photo-186599306_457239281')
				if users[user_id].photo == 13:
					photo(id, 'photo-186599306_457239271')
				if users[user_id].photo == 14:
					photo(id, 'photo-186599306_457239258')
				if users[user_id].photo == 15:
					photo(id, 'photo-186599306_457239256')
				if users[user_id].photo == 16:
					photo(id, 'photo-186599306_457239251')
				if users[user_id].photo == 17:
					photo(id, 'photo-102526299_457239628')
				if users[user_id].photo == 18:
					photo(id, 'photo-102526299_457239594')
				if users[user_id].photo == 19:
					photo(id, 'photo-102526299_456239523')