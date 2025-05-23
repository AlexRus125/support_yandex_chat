from generate_logic import generate_random_platform
import random

def main():




    #! Важно: все, что закомментировано, это мои исправления ошибок в коде, почему не убрал, потому что чтобы не забыть что исправил, все работает

    #Создали платформы со случайными чатами, пользователями и операторами
    platform = generate_random_platform(num_operators=40, num_users=100, num_chats=100)


    # print(f"Чат всего: {len(platform.chats)}")
    # if platform.chats:
    #     first_chat = platform.chats[0]
    #     print(f"Первый чат: {'открыт' if first_chat.is_open else 'закрыт'}")
    #     print(f"Оценка: {first_chat.csat}")
    #     print(f"Сообщений: {len(first_chat.messages)}")
    # else:
    #     print("Не получилось создать, надо исправить.")

    # platform = generate_random_platform(num_operators=15, num_users=50, num_chats=50)
    #
    # # Проверка статуса операторов
    # for op in platform.operators:
    #     print(f"{op.get_full_name}: {'Свободен' if op.is_available else 'Занят'}")
    #
    # # Проверка чатов
    # print(f"Всего чатов: {len(platform.chats)}")
    # print(f"Открытых чатов: {sum(1 for c in platform.chats if c.is_open)}")
    # print(f"Закрытых чатов: {sum(1 for c in platform.chats if not c.is_open)}")

    # total_chats = len(platform.chats)
    # open_chats = sum(1 for chat in platform.chats if chat.is_open)
    # closed_with_csat = sum(1 for chat in platform.chats if not chat.is_open and chat.csat is not None)
    # closed_no_csat = sum(1 for chat in platform.chats if not chat.is_open and chat.csat is None)




    #Вывод в консоль разных данных
    print(f"Сгенерировано операторов: {len(platform.operators)}")
    print(f"Сгенерировано пользователей: {len(platform.users)}")
    print(f"Сгенерировано чатов: {len(platform.chats)}")
    print(f"Открытых чатов: {len([c for c in platform.chats if c.is_open])}")
    print(f"Закрытых чатов с оценкой: {len([c for c in platform.chats if not c.is_open and c.csat is not None])}")
    print(f"Закрытых чатов без оценки: {len([c for c in platform.chats if not c.is_open and c.csat is None])}")


    #Полная информация об случайном операторе
    some_operator = random.choice(platform.operators)
    platform.export_chats_operator(some_operator)

    #Полная информация о случайном пользователе
    some_user = random.choice(platform.users)
    platform.export_chats_user(some_user)

    # Экспорт данных
    # print("\nЭкспорт данных:")
    # platform.export_chats()
    # platform.export_operators()
    # platform.export_users()





if __name__ == '__main__':
    main()












