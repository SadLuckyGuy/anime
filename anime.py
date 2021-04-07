import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
import random

vk_session = vk_api.VkApi(token = '422f0a77cb543213ab9ef515b7c4939adecbdb5904d4ab69e9a8b8846593a7c00165c7b552c50401c7bba') 
# 422f0a77cb543213ab9ef515b7c4939adecbdb5904d4ab69e9a8b8846593a7c00165c7b552c50401c7bba - TEST
# c41c3b0142af57ad5b28f76bfcf7bbb54f25133e83e579921b886a06b47221d07892379a62e92f5a92656 - SadBot
# a863cfe7e14425f41abd4890340ea94e5ee063293ab648a97f09a506433f8c540006c219dd43b49b8e55c - Хлам питонщика
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
		self.number = 0

	def tokya(self, event):
		self.event = event
		self.stats = 1

	def list(self, event):
		self.event = event
		self.ser += 1

	def undo(self, event):
		self.event = event
		self.ser -= 1

	def go(self, event):
		self.event = event
		self.manga += 1

	def back(self, event):
		self.event = event
		self.manga -= 1

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
			[get_but('Токийский гуль', 'negative')],
			[get_but('Атака титанов', 'positive')],
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

back_key = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Назад', 'negative')],
	]
}

back_key = json.dumps(back_key, ensure_ascii = False).encode('utf-8')
back_key = str(back_key.decode('utf-8'))

photo_key = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Фото', 'positive')],
	]
}

photo_key = json.dumps(photo_key, ensure_ascii = False).encode('utf-8')
photo_key = str(photo_key.decode('utf-8'))

ataka = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Манга', 'positive')],
	]
}

ataka = json.dumps(ataka, ensure_ascii = False).encode('utf-8')
ataka = str(ataka.decode('utf-8'))

welcome = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Перелистнуть вперед', 'positive')],
	]
}

welcome = json.dumps(welcome, ensure_ascii = False).encode('utf-8')
welcome = str(welcome.decode('utf-8'))

forma = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Перелистнуть вперед', 'positive')],
		[get_but('Перелистнуть назад', 'negative')],
	]
}

forma = json.dumps(forma, ensure_ascii = False).encode('utf-8')
forma = str(forma.decode('utf-8'))

back = {
	'one_time' : True,
	'inline' : False,
	'buttons' : [
		[get_but('Перелистнуть назад', 'negative')],
		[get_but('Меню', 'positive')]
	]
}

back = json.dumps(back, ensure_ascii = False).encode('utf-8')
back = str(back.decode('utf-8'))

users = {}
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		msg = event.text.lower()
		id = event.user_id
		user_id = session_api.messages.getById(message_ids = event.message_id)['items'][0]['from_id']

		if users.get(user_id) == None:
			users[user_id] = User(msg)

		if msg == 'проверка1':
			users[user_id].go(event)

		if msg == 'проверка':
			sender(id, 'Манга: ' + str(users[user_id].manga))

		if msg == 'аниме':
			vk_session.method('messages.send', {'user_id' : id, 'message' : 'Доступные аниме:' + '\n💔Токийский гуль' + '\n⚔Атака титанов', 'keyboard' : anime_key, 'random_id' : random.randint(-12424235, +1245242)})

		if msg == 'атака титанов':
			users[user_id].stats = 2
			vk_session.method('messages.send', {'user_id' : id, 'message' : 'Доступно:' + '\n📜Манга', 'keyboard': ataka, 'random_id' : random.randint(-1234567, +1234567)})

		if msg == 'манга':
			if users[user_id].stats == 2:
				sender(id, 'Выберите главу манги (доступно только 127)')

		if msg == '127':
			if users[user_id].stats == 2:
				users[user_id].number = 127
				photo(id, 'photo-202584478_457239073')
				vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть', 'keyboard' : welcome, 'random_id' : random.randint(-1234567, +1234567)})

		if msg == 'перелестнуть вперед':
			if users[user_id].stats == 2:
				if users[user_id].number == 127:
					users[user_id].go(event)
					if users[user_id].manga == 1:
						photo(id, 'photo-202584478_457239074')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед', 'keyboard' : welcome, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 2:
						photo(id, 'photo-202584478_457239075')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 3:
						photo(id, 'photo-202584478_457239076')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 4:
						photo(id, 'photo-202584478_457239077')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 5:
						photo(id, 'photo-202584478_457239078')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 6:
						photo(id, 'photo-202584478_457239079')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 7:
						photo(id, 'photo-202584478_457239080')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 8:
						photo(id, 'photo-202584478_457239081')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 9:
						photo(id, 'photo-202584478_457239082')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 10:
						photo(id, 'photo-202584478_457239083')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 11:
						photo(id, 'photo-202584478_457239084')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 12:
						photo(id, 'photo-202584478_457239085')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 13:
						photo(id, 'photo-202584478_457239086')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 14:
						photo(id, 'photo-202584478_457239087')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 15:
						photo(id, 'photo-202584478_457239088')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 16:
						photo(id, 'photo-202584478_457239089')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 17:
						photo(id, 'photo-202584478_457239090')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 18:
						photo(id, 'photo-202584478_457239091')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 19:
						photo(id, 'photo-202584478_457239092')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 20:
						photo(id, 'photo-202584478_457239093')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 21:
						photo(id, 'photo-202584478_457239094')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 22:
						photo(id, 'photo-202584478_457239095')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 23:
						photo(id, 'photo-202584478_457239096')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 24:
						photo(id, 'photo-202584478_457239097')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 25:
						photo(id, 'photo-202584478_457239098')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 26:
						photo(id, 'photo-202584478_457239099')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 27:
						photo(id, 'photo-202584478_457239100')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 28:
						photo(id, 'photo-202584478_457239101')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 29:
						photo(id, 'photo-202584478_457239102')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 30:
						photo(id, 'photo-202584478_457239103')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 31:
						photo(id, 'photo-202584478_457239104')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 32:
						photo(id, 'photo-202584478_457239105')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 33:
						photo(id, 'photo-202584478_457239106')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 34:
						photo(id, 'photo-202584478_457239107')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 35:
						photo(id, 'photo-202584478_457239108')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 36:
						photo(id, 'photo-202584478_457239109')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 37:
						photo(id, 'photo-202584478_457239110')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 38:
						photo(id, 'photo-202584478_457239111')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 39:
						photo(id, 'photo-202584478_457239112')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 40:
						photo(id, 'photo-202584478_457239113')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 41:
						photo(id, 'photo-202584478_457239114')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 42:
						photo(id, 'photo-202584478_457239115')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 43:
						photo(id, 'photo-202584478_457239116')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 44:
						photo(id, 'photo-202584478_457239117')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Конец "127" главы', 'keyboard' : back, 'random_id' : random.randint(-1234567, +1234567)})

		if msg == '128':
			if users[user_id].stats == 2:
				users[user_id].number = 128
				photo(id, 'photo-202584478_457239073')
				vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть', 'keyboard' : welcome, 'random_id' : random.randint(-1234567, +1234567)})

		if msg == 'перелестнуть вперед':
			if users[user_id].stats == 2:
				if users[user_id].number == 128:
					users[user_id].go(event)
					if users[user_id].manga == 1:
						photo(id, 'photo-202584478_457239119') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед', 'keyboard' : welcome, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 2:
						photo(id, 'photo-202584478_457239120') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 3:
						photo(id, 'photo-202584478_457239121') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 4:
						photo(id, 'photo-202584478_457239122') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 5:
						photo(id, 'photo-202584478_457239123') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 6:
						photo(id, 'photo-202584478_457239124') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 7:
						photo(id, 'photo-202584478_457239125')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 8:
						photo(id, 'photo-202584478_457239126') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 9:
						photo(id, 'photo-202584478_457239127') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 10:
						photo(id, 'photo-202584478_457239128') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 11:
						photo(id, 'photo-202584478_457239129') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 12:
						photo(id, 'photo-202584478_457239130') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 13:
						photo(id, 'photo-202584478_457239131') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 14:
						photo(id, 'photo-202584478_457239132') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 15:
						photo(id, 'photo-202584478_457239133') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 16:
						photo(id, 'photo-202584478_457239134') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 17:
						photo(id, 'photo-202584478_457239135')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 18:
						photo(id, 'photo-202584478_457239136') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 19:
						photo(id, 'photo-202584478_457239137') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 20:
						photo(id, 'photo-202584478_457239138') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 21:
						photo(id, 'photo-202584478_457239139') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 22:
						photo(id, 'photo-202584478_457239140') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 23:
						photo(id, 'photo-202584478_457239141') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 24:
						photo(id, 'photo-202584478_457239142')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 25:
						photo(id, 'photo-202584478_457239143') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 26:
						photo(id, 'photo-202584478_457239144') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 27:
						photo(id, 'photo-202584478_457239145') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 28:
						photo(id, 'photo-202584478_457239146')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 29:
						photo(id, 'photo-202584478_457239147') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 30:
						photo(id, 'photo-202584478_457239157') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 31:
						photo(id, 'photo-202584478_457239158') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 32:
						photo(id, 'photo-202584478_457239159') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 33:
						photo(id, 'photo-202584478_457239160') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 34:
						photo(id, 'photo-202584478_457239161') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 35:
						photo(id, 'photo-202584478_457239162') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 36:
						photo(id, 'photo-202584478_457239163') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 37:
						photo(id, 'photo-202584478_457239164')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 38:
						photo(id, 'photo-202584478_457239165') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 39:
						photo(id, 'photo-202584478_457239167') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 40:
						photo(id, 'photo-202584478_457239168') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 41:
						photo(id, 'photo-202584478_457239169') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 42:
						photo(id, 'photo-202584478_457239170') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 43:
						photo(id, 'photo-202584478_457239171') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 44:
						photo(id, 'photo-202584478_457239172')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Конец "128" главы', 'keyboard' : back, 'random_id' : random.randint(-1234567, +1234567)})
		
		if msg == 'перелестнуть назад':
			if users[user_id].stats == 2:
				if users[user_id].number == 127:
					users[user_id].back(event)
					if users[user_id].manga == 1:
						photo(id, 'photo-202584478_457239074')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед', 'keyboard' : welcome, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 2:
						photo(id, 'photo-202584478_457239075')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 3:
						photo(id, 'photo-202584478_457239076')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 4:
						photo(id, 'photo-202584478_457239077')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 5:
						photo(id, 'photo-202584478_457239078')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 6:
						photo(id, 'photo-202584478_457239079')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 7:
						photo(id, 'photo-202584478_457239080')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 8:
						photo(id, 'photo-202584478_457239081')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 9:
						photo(id, 'photo-202584478_457239082')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 10:
						photo(id, 'photo-202584478_457239083')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 11:
						photo(id, 'photo-202584478_457239084')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 12:
						photo(id, 'photo-202584478_457239085')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 13:
						photo(id, 'photo-202584478_457239086')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 14:
						photo(id, 'photo-202584478_457239087')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 15:
						photo(id, 'photo-202584478_457239088')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 16:
						photo(id, 'photo-202584478_457239089')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 17:
						photo(id, 'photo-202584478_457239090')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 18:
						photo(id, 'photo-202584478_457239091')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 19:
						photo(id, 'photo-202584478_457239092')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 20:
						photo(id, 'photo-202584478_457239093')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 21:
						photo(id, 'photo-202584478_457239094')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 22:
						photo(id, 'photo-202584478_457239095')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 23:
						photo(id, 'photo-202584478_457239096')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 24:
						photo(id, 'photo-202584478_457239097')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 25:
						photo(id, 'photo-202584478_457239098')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 26:
						photo(id, 'photo-202584478_457239099')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 27:
						photo(id, 'photo-202584478_457239100')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 28:
						photo(id, 'photo-202584478_457239101')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 29:
						photo(id, 'photo-202584478_457239102')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 30:
						photo(id, 'photo-202584478_457239103')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 31:
						photo(id, 'photo-202584478_457239104')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 32:
						photo(id, 'photo-202584478_457239105')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 33:
						photo(id, 'photo-202584478_457239106')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 34:
						photo(id, 'photo-202584478_457239107')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 35:
						photo(id, 'photo-202584478_457239108')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 36:
						photo(id, 'photo-202584478_457239109')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 37:
						photo(id, 'photo-202584478_457239110')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 38:
						photo(id, 'photo-202584478_457239111')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 39:
						photo(id, 'photo-202584478_457239112')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 40:
						photo(id, 'photo-202584478_457239113')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 41:
						photo(id, 'photo-202584478_457239114')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 42:
						photo(id, 'photo-202584478_457239115')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 43:
						photo(id, 'photo-202584478_457239116')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
		if msg == 'перелестнуть назад':
			if users[user_id].stats == 2:
				if users[user_id].number == 128:
					users[user_id].back(event)
					if users[user_id].manga == 1:
							photo(id, 'photo-202584478_457239119') 
							vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед', 'keyboard' : welcome, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 2:
						photo(id, 'photo-202584478_457239120') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 3:
						photo(id, 'photo-202584478_457239121') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 4:
						photo(id, 'photo-202584478_457239122') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 5:
						photo(id, 'photo-202584478_457239123') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 6:
						photo(id, 'photo-202584478_457239124') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 7:
						photo(id, 'photo-202584478_457239125')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 8:
						photo(id, 'photo-202584478_457239126') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 9:
						photo(id, 'photo-202584478_457239127') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 10:
						photo(id, 'photo-202584478_457239128') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 11:
						photo(id, 'photo-202584478_457239129') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 12:
						photo(id, 'photo-202584478_457239130') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 13:
						photo(id, 'photo-202584478_457239131') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 14:
						photo(id, 'photo-202584478_457239132') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 15:
						photo(id, 'photo-202584478_457239133') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 16:
						photo(id, 'photo-202584478_457239134') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 17:
						photo(id, 'photo-202584478_457239135')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 18:
						photo(id, 'photo-202584478_457239136') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 19:
						photo(id, 'photo-202584478_457239137') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 20:
						photo(id, 'photo-202584478_457239138') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 21:
						photo(id, 'photo-202584478_457239139') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 22:
						photo(id, 'photo-202584478_457239140') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 23:
						photo(id, 'photo-202584478_457239141') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 24:
						photo(id, 'photo-202584478_457239142')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 25:
						photo(id, 'photo-202584478_457239143') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 26:
						photo(id, 'photo-202584478_457239144') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 27:
						photo(id, 'photo-202584478_457239145') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 28:
						photo(id, 'photo-202584478_457239146')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 29:
						photo(id, 'photo-202584478_457239147') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 30:
						photo(id, 'photo-202584478_457239157') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 31:
						photo(id, 'photo-202584478_457239158') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 32:
						photo(id, 'photo-202584478_457239159') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 33:
						photo(id, 'photo-202584478_457239160') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 34:
						photo(id, 'photo-202584478_457239161') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 35:
						photo(id, 'photo-202584478_457239162') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 36:
						photo(id, 'photo-202584478_457239163') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 37:
						photo(id, 'photo-202584478_457239164')  
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 38:
						photo(id, 'photo-202584478_457239165') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 39:
						photo(id, 'photo-202584478_457239167') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 40:
						photo(id, 'photo-202584478_457239168') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 41:
						photo(id, 'photo-202584478_457239169') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 42:
						photo(id, 'photo-202584478_457239170') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 43:
						photo(id, 'photo-202584478_457239171') 
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Используйте "Перелистнуть вперед", чтобы перелистнуть вперед' + '\nИспользуйте "Перелистнуть назад", чтобы перелистнуть назад', 'keyboard' : forma, 'random_id' : random.randint(-1234567, +1234567)})
					if users[user_id].manga == 44:
						photo(id, 'photo-202584478_457239172')
						vk_session.method('messages.send', {'user_id' : id, 'message' : 'Конец "128" главы', 'keyboard' : back, 'random_id' : random.randint(-1234567, +1234567)})



		if msg == 'токийский гуль':
			users[user_id].stats = 1
			if users[user_id].stats == 1:
				vk_session.method('messages.send', {'user_id' : id, 'message' : 'Доступно:' + '\n🎬Серии' + '\n📷Фото (рандомное фото)', 'keyboard' : tokya_key, 'random_id' : random.randint(-12424235, +1245242)})
		
		elif msg == 'серии':
			if users[user_id].stats == 1:
				sender(id, '1 СЕЗОН:' + '\n1 серия - Трагедия - 3 июля 2014' + '\n2 серия - Вылупление - 10 июля 2014 года' + '\n3 серия - Белый голубь - 17 июля - 2014 года' + '\n4 серия - Ужин - 24 июля 2014 года' + '\n5 серия - Шрам - 31 июля 2014 года' + "\n6 серия - Ливень - 7 августа 2014 года")
				vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Пленение - 14 августа 2014 года' + "\n8 серия - Цикл - 21 августа 2014 года" + "\n9 серия - Птичья клетка - 28 августа 2014 года" + "\n10 серия - Аогири - 4 сентября 2014 года" + "\n11 серия - Боевой дух - 11 сентября 2014 года" + '\n12 серия - Гуль - 18 сентября 2014 года', 'keyboard' : listen_key, 'random_id' : random.randint(-12424235, +1245242)})
				users[user_id].ser = 0

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
					vk_session.method('messages.send', {'user_id' : id, 'message' : '7 серия - Узы - 20 ноября 2018' + '\n8 серия - Пробуждённое дитя - 27 ноября 2018' + '\n9 серия - Напоминание - 4 декабря 2018' + '\n10 серия - Конец трагедии - 11 декабря 2018' + '\n11 серия - Столкновение - 18 декабря 2018' + '\n12 серия - Финал - 25 декабря 2018', 'keyboard' : back_key, 'random_id' : random.randint(-12424235, +1245242)})


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
				users[user_id].photo = random.randint(1, 45)
				if users[user_id].photo == 1:
					photo(id, 'photo-202584478_457239028')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 2:
					photo(id, 'photo-202584478_457239029')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 3:
					photo(id, 'photo-202584478_457239030')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 4:
					photo(id, 'photo-202584478_457239031')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 5:
					photo(id, 'photo-202584478_457239032')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 6:
					photo(id, 'photo-202584478_457239033')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 7:
					photo(id, 'photo-202584478_457239034')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 8:
					photo(id, 'photo-202584478_457239035')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 9:
					photo(id, 'photo-202584478_457239036')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 10:
					photo(id, 'photo-202584478_457239037')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 11:
					photo(id, 'photo-202584478_457239038')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 12:
					photo(id, 'photo-202584478_457239039')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 13:
					photo(id, 'photo-202584478_457239040')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 14:
					photo(id, 'photo-202584478_457239041')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 15:
					photo(id, 'photo-202584478_457239042')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 16:
					photo(id, 'photo-202584478_457239043')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 17:
					photo(id, 'photo-202584478_457239044')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 18:
					photo(id, 'photo-202584478_457239045')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 19:
					photo(id, 'photo-202584478_457239046')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 20:
					photo(id, 'photo-202584478_457239047')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 21:
					photo(id, 'photo-202584478_457239048')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 22:
					photo(id, 'photo-202584478_457239049')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 23:
					photo(id, 'photo-202584478_457239050')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 24:
					photo(id, 'photo-202584478_457239051')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 25:
					photo(id, 'photo-202584478_457239052')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 26:
					photo(id, 'photo-202584478_457239053')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 27:
					photo(id, 'photo-202584478_457239054')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 28:
					photo(id, 'photo-202584478_457239055')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 29:
					photo(id, 'photo-202584478_457239056')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 30:
					photo(id, 'photo-202584478_457239057')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 31:
					photo(id, 'photo-202584478_457239058')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 32:
					photo(id, 'photo-202584478_457239059')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 33:
					photo(id, 'photo-202584478_457239060')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 34:
					photo(id, 'photo-202584478_457239061')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 35:
					photo(id, 'photo-202584478_457239062')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 36:
					photo(id, 'photo-202584478_457239063')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 37:
					photo(id, 'photo-202584478_457239064')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 38:
					photo(id, 'photo-202584478_457239065')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 39:
					photo(id, 'photo-202584478_457239066')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 40:
					photo(id, 'photo-202584478_457239067')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 41:
					photo(id, 'photo-202584478_457239068')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 42:
					photo(id, 'photo-202584478_457239069')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 43:
					photo(id, 'photo-202584478_457239070')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 44:
					photo(id, 'photo-202584478_457239071')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})
				if users[user_id].photo == 45:
					photo(id, 'photo-202584478_457239072')
					vk_session.method('messages.send', {'user_id' : id, 'message' : 'Напишите "фото", чтобы посмотреть еще фотографий', 'keyboard' : photo_key, 'random_id' : random.randint(-1242412, +1242412)})