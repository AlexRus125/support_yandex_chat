from person import Person


class Operator(Person):

    '''Класс для операторов, который наследует данные из класса Person'''

    def __init__(self, name: str, middle_name: str, last_name: str, city: str, birth_date: str, position: str, experience: int):  #Иницииализируем доп свойства в классе Operator: position, experience
        super().__init__(name, middle_name, last_name, city, birth_date)

        self.position = position
        self.experience = experience
        self.is_available = True
        self.chats_count = []



    def data_json(self):
        'Возможность хранить данные в об операторе в json формате'
        data_operator = super().data_json()
        data_operator.update({
            'Должность' : self.position,
            'Стаж_работы': self.experience,
            'Свободность': self.is_available,
            'Кол-во_обработанных_чатов': len(self.chats_count)
        })

        return data_operator


