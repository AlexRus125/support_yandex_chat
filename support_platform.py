import random

from oper import Operator
from user import User
from chat import Chat
from typing import Optional, List
import json



class SupportPlatform:

    '''Место где решаются ваши вопросы

    Класс платформы поддержки
    '''

    def __init__(self):
        self.operators: List[Operator] = []
        self.users: List[User] = []
        self.chats: List[Chat] = []


    def add_operator(self, operator: Operator):
        '''Добавляем операторов на платформу'''
        self.operators.append(operator)

    def add_user(self, user: User):
        '''Добавляем пользователей на платформу'''
        self.users.append(user)

    def create_chat(self, user: User):
        '''Проверка на доступность операторов'''
        available_operators = [op for op in self.operators if op.is_available]
        print(f"Доступно операторов: {len(available_operators)}")

        if len(available_operators) == 0:
            return None

        operator = random.choice(available_operators)
        operator.is_available = False
        chat = Chat(user, operator)
        user.created_chats.append(chat)
        operator.chats_count.append(chat)
        self.chats.append(chat)
        print(f"Создан чат: {user.get_full_name} -> {operator.get_full_name}")
        return chat


    def close_chat(self, chat: Chat, csat:Optional[int] = None):

        chat.close_chat(csat)
        chat.operator.is_available = True


    def export_chats(self, file_name = 'export_chats.json'):

        data = [chat.data_json() for chat in self.chats]
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Экспортировано {len(data)} чатов в {file_name}")



    def export_chats_operator(self, operator: Operator, file_name='export_operators_chats.json'):

        data = [chat.data_json() for chat in self.chats if chat.operator == operator]

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Экспортировано {len(data)} чатов оператора {operator.get_full_name} в {file_name}")




    def export_chats_user(self, user: User, file_name = 'export_user_chats.json'):

        data = [chat.data_json() for chat in self.chats if chat.user == user]

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Экспортировано {len(data)} чатов пользователя {user.get_full_name} в {file_name}")


    def export_operators(self, file_name = 'export_operators.json'):

        data = [operator.data_json() for operator in self.operators]

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Экспортировано {len(data)} операторов в {file_name}")

    def export_users(self, file_name = 'export_users.json'):
        data = [user.data_json() for user in self.users]

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Экспортировано {len(data)} пользователей в {file_name}")












