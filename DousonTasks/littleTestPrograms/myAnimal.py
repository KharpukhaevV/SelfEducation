# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pas_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и я чувствую себя", self.mood, )
        self.__pas_time()

    def eat(self, food=4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pas_time()

    def play(self, fun=4):
        print("Уиии..")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pas_time()


def main():
    crit_name = input("Как вы назовете свою зверушку: ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print(
            """
            Моя зверушка
            0 - Выйти
            1 - Узнать о самочувствии зверюшки
            2 - Покормить зверушку
            3 - Поиграть со зверушкой
            """
        )
        choice = input("Ваш выбор:")
        print()
        # Выход
        if choice == "0":
            print("До свидания")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            eat_value = input("Сколько раз покормить зверушку: ")
            if eat_value != "":
                crit.eat(int(eat_value))
            else:
                crit.eat()
        elif choice == "3":
            play_value = input("Сколько раз поиграть: ")
            if play_value != "":
                crit.play(int(play_value))
            else:
                crit.play()
        else:
            print("Извините, в меню нет такого пункта")


main()
