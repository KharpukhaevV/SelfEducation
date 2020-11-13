print("Программа считалка")
start = int(input("Введите начало счета: "))
finish = int(input("Введите конец счета: "))
interval = int(input("Введите интервал счета: "))
for i in range(start, finish, interval):
    print(i, end=" ")
input("Нажмите Enter для выхода")


