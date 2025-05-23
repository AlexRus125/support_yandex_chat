from oper import Operator
from user import User
from datetime import datetime
from typing import List, Optional
from message import Message


class Chat:
    '''Класс чата, где будет общаться пользователь и оператор'''
    def __init__(self, user: User, operator: Operator):

        self.user = user
        self.operator = operator
        self.is_open = True
        self.time_created = datetime.now()
        self.time_closed: Optional[datetime] = None
        self.csat = None
        self.messages: List[Message] = []



    def add_message(self, sender: str, text: str):
        'Пользователь и оператор могут добавлять сообщения'
        message = Message(sender, text, datetime.now())
        self.messages.append(message)

    def close_chat(self, csat):
        'Метод для оценки помощи'
        self.is_open = False
        self.time_closed = datetime.now()
        if (csat is not None) and (1 <= csat <= 5):
            self.csat = csat

    def data_json(self):

        data = {
            'Пользователь': self.user.data_json(),
            'Оператор': self.operator.data_json(),
            'Чат_создан_в': self.time_created.strftime("%d %m %Y., %H:%M:%S"),
            'Чат_закрыт_в': self.time_closed.strftime("%d %m %Y., %H:%M:%S") if self.time_closed is not None else None,
            'Оценка_чата': self.csat,
            'Открытость_чата' : self.is_open,
            'Сообщения_в_чате':[msg.data_json() for msg in self.messages]

        }


        return data























