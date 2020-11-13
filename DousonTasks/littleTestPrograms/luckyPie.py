import random

print("Возмите пирожок с сюрпризом")
pie = random.randint(1, 5)
input("Нажмите Enter что бы выбрать пирожок")
if pie == 1:
    print("Ваше предсказание 1")
elif pie == 2:
    print("Ваше предсказание 2")
elif pie == 3:
    print("Ваше предсказание 3")
elif pie == 4:
    print("Ваше предсказание 4")
else:
    print("Ваше предсказание 5")
input("Нажмите Enter что бы выйти")
