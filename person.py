class Person:
    '''Класс-родитель, базовый класс для пользователей и операторов'''

    def __init__(self, name: str, middle_name: str, last_name: str, city: str, birth_date: str):

        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.city = city
        self.birth_date = birth_date

    @property
    def get_full_name(self):

        return f'{self.name} {self.middle_name} {self.last_name}'

    def data_json(self):
        'для сохранения данных в json формате'
        data = {'Имя':self.name,
                'Фамилия': self.middle_name,
                'Отчество': self.last_name
                }

        return data



