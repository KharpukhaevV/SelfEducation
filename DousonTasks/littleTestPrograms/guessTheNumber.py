import random


def ask_number(question):
    """Просит ввести число из дивпазона."""
    response = None
    while response not in range(1, 101):
        response = int(input(question))
    return response


def main():
    print("Я загадаю число от 1 до 100, а ты попробуй отгадать его за 8 попыток")
    input("Нажми Enter что бы начать")
    guessNumber = random.randint(1, 100)
    attempts = 1
    number = None
    while attempts < 9 and number != guessNumber:
        number = ask_number("Введите число: ")
        if number < guessNumber:
            print("Загаданное число больше, у вас осталось", 8 - attempts, "попыток")
        elif number > guessNumber:
            print("Загаданное число меньше, у вас осталось", 8 - attempts, "попыток")
        attempts += 1
    if attempts > 8:
        print("Попытки кончились, вы проиграли")
    else:
        print("Ура вы отгадали у вас ушло", attempts, "попыток")


main()
