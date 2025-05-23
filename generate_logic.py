import random
from support_platform import SupportPlatform
from oper import Operator
from user import User


'''
В этом файле сгенерируем
случайные данные пользователя
'''

def generate_random_name():

    '''Генерируем случайных людей'''

    name = ['Анастасия', 'Георгий', 'Степан', 'Павел', 'Аполлон', 'Юлия', 'Екатерина', 'Светлана', 'Елизавета', 'Александр', 'Надежда']

    surname = ['Медведева', 'Купельский', 'Тарантин', 'Петров', 'Иванов', 'Боровикова', 'Копылова', 'Паншина', 'Новоселова', 'Смыкова', 'Прокофьев']

    lastname = ["Иванович", "Алексеевич", "Дмитриевич", "Сергеевич", "Андреевич", "Ивановна", "Алексеевна", "Дмитриевна", "Сергеевна", "Андреевна", "Анатольевна"]


    return (
        random.choice(name),
        random.choice(surname),
        random.choice(lastname)
    )


def generate_random_position():

    '''Создаем случайные должности'''

    positions = ['л1(агент)', 'л2(другое)', 'л2(платежи)', 'л2(антифрод)', 'тимлидер', 'наставник', 'ментор']


    return random.choice(positions)



def generate_random_date(start_year=1900, end_year=2010):

    '''Создаем случайную дату обращений'''

    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  #Сделал так, потому что 28 дней точно есть во всех месяцах, а вот 30 и 31 не везде


    return f'{year}-{month:02d}-{day:02d}'


def generate_random_text():
    '''Генерация рандомного текста'''
    texts = [
        'Где мой заказ',
        'Почему курьер опять опаздывает',
        'Не хватает позиции',
        'Мне привезли не мой заказ',
        'Как мне оставить жалобу на курьера',
        'Как применить промокод',
        'Не применился промокод'
    ]


    return random.choice(texts)



def generate_random_city():

    """Генерация случайного города"""
    cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
             "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону"]
    return random.choice(cities)




def generate_random_platform(num_operators=20, num_users=100, num_chats=150):
    """Генерация случайной платформы с операторами, пользователями и чатами"""
    platform = SupportPlatform()

    # Генерация операторов
    for _ in range(num_operators):
        name, last_name, middle_name = generate_random_name()
        operator = Operator(
            name=name,
            last_name=last_name,
            middle_name=middle_name,
            city=generate_random_city(),
            birth_date=generate_random_date(1980, 1995),
            position=generate_random_position(),
            experience=random.randint(1, 10)
        )
        platform.add_operator(operator)

    # Генерация пользователей
    for _ in range(num_users):
        name, last_name, middle_name = generate_random_name()
        user = User(
            name=name,
            last_name=last_name,
            middle_name=middle_name,
            city=generate_random_city(),
            birth_date=generate_random_date(1985, 2005)
        )
        platform.add_user(user)

    # Генерация чатов
    for _ in range(num_chats):
        user = random.choice(platform.users)
        chat = platform.create_chat(user)
        if chat:
            # Добавляем сообщения в чат
            num_messages = random.randint(1, 10)
            for i in range(num_messages):
                if i % 2 == 0:
                    sender = user.get_full_name
                else:
                    sender = chat.operator.get_full_name
                chat.add_message(sender, generate_random_text())

            # Случайно закрываем некоторые чаты с оценкой
            #Сделано для того, чтобы какие чаты получали csat а какие-то нет
            if random.random() > 0.4:  # 60% чатов закрываются
                csat = random.randint(1, 5) if random.random() > 0.2 else None    # с 20% шансом пользователь поставит оценочку
                platform.close_chat(chat, csat)
                #Сделал проверку чтобы посмотреть в выводе
                print(f"Чат закрыт. Оценка: {csat}")
            else:
                print("Чат остался открытым")

    return platform



















