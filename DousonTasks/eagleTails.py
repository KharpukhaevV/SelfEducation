import random

print("Я подброшу монетку 100 раз и скажу сколько раз выпал орел или решка")
eagle = 0
tails = 0
flips = 0
input("Нажмите Enter что бы продолжить")
while flips != 100:
    coin = random.randint(1, 2)
    if coin == 1:
        eagle += 1
    else:
        tails += 1
    flips += 1
print("Орел выпал ", eagle, "раз, решка выпала", tails, "раз")
input("Нажмите Enter что бы выйти")
