class Tv(object):
    """Имитация телевизора"""
    def __init__(self, channel=1, volume=5):
        self.channel = channel
        self.volume = volume

    def change_channel(self, change):
        if change == "+" and self.channel+1 <= 25:
            self.channel += 1
        elif change == "-" and self.channel-1 > 0:
            self.channel -= 1
        elif type(change) == int:
            self.channel = change
        print("Сейчас показывает канал №", self.channel)

    def change_volume(self, change):
        if change == "+" and self.volume+1 <= 25:
            self.volume += 1
        elif change == "-" and self.volume-1 >= 0:
            self.volume -= 1
        print("Громкость равна", self.volume)


def main():
    my_tv = Tv()
    choice = None
    while choice != "0":
        print(
            """
            Мой телевизор
            0 - Выйти
            1 - Следующий канал
            2 - Предыдущий канал
            3 - Ввести номер канала
            4 - Прибавить громкость
            5 - Убавить громкость
            """
        )
        choice = input("Ваш выбор:")
        if choice == "0":
            print("До свидания")
        elif choice == "1":
            my_tv.change_channel("+")
        elif choice == "2":
            my_tv.change_channel("-")
        elif choice == "3":
            try:
                num_channel = int(input("Введите номер канала: "))
                my_tv.change_channel(num_channel)
            except ValueError:
                print("Невернное значение канала")
        elif choice == "4":
            my_tv.change_volume("+")
        elif choice == "5":
            my_tv.change_volume("-")


main()
