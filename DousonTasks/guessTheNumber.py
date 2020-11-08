import random


def manGuessNum():
    print("Я загадаю число от 1 до 100, а ты попробуй отгадать его за 8 попыток")
    input("Нажми Enter что бы начать")
    guessNumber = random.randint(1, 100)
    attempts = 1
    number = 0
    while attempts < 9 and number != guessNumber:
        number = int(input("Введите число:"))
        if number < guessNumber:
            print("Загаданное число больше, у вас осталось", 8 - attempts, "попыток")
        elif number > guessNumber:
            print("Загаданное число меньше, у вас осталось", 8 - attempts, "попыток")
        attempts += 1
    if attempts > 8:
        print("Попытки кончились, вы проиграли")
    else:
        print("Ура вы отгадали у вас ушло", attempts, "попыток")
