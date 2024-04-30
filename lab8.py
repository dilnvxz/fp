import random

def greeting():
    """Функция для приветствия пользователя."""

    responses = ["Привет! Чем могу помочь?", "Здравствуйте! Чем могу быть полезен?", "Приветствую! Чем могу помочь вам сегодня?"]
    return random.choice(responses)

def farewell():
    """Функция для прощания с пользователем."""
    responses = ['До свидания! Надеюсь, вы вернетесь снова.', 'Пока! Жду вас в следующий раз.', 'До встречи!']
    return random.choice(responses)

def process_message(message):
    """Функция для обработки сообщений пользователя."""
    message = message.lower()
    if "привет" in message:
        return greeting()
    elif "пока" in message:
        return farewell()
    else:
        return "Извините, я не понимаю. Могу ли я вам помочь чем-то еще?"

def main():
    """Основная функция для запуска чат-бота."""
    print("Добро пожаловать в функциональный чат-бот!")
    while True:
        user_input = input("Вы: ")
        response = process_message(user_input)
        print("Чат-бот:", response)
        if "пока" in user_input.lower():
            break

if __name__ == "__main__":
    main()



