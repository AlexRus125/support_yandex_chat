from datetime import datetime



class Message:

    '''Класс сообщения, которое поступает в чат'''

    def __init__(self, sender: str, text: str, sending_time: datetime):

        self.sender = sender
        self.text = text
        self.sending_time = sending_time


    def data_json(self):

        data = {
            'Оправитель': self.sender,
            'Сообщение': self.text,
            'Время_отправки': self.sending_time.strftime("%d %m %Y., %H:%M:%S")
        }


        return data



