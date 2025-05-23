from person import Person



class User(Person):
    '''Класс пользователя сервисом'''

    def __init__(self, name: str, middle_name: str, last_name: str, city: str, birth_date: str):
        super(User, self).__init__(name, middle_name, last_name, city, birth_date)

        self.created_chats = []



    def data_json(self):
        data_user = super().data_json()
        data_user.update({
            'Кол-во_созданных_чатов': len(self.created_chats)
        })


        return data_user




















