familyTree = {"джейден смит": "уилл смит",
              "эмма робертс": "эрик робертс",
              "колин хэнкс": "том хэнкс",
              "чарли шин": "мартин шин",
              "майкл дуглас": "кирк дуглас",
              "владимир харпухаев": "яков харпухаев",
              "яков харпухаев": "ярба харпухаев",
              "игорь горбунов": "олег горбунов",
              "олег горбунов": "евгений горбунов"
              }
choice = None
while choice != 0:
    print(
        """
        0 - Выйти.
        1 - Кто твой отец?
        2 - Кто твой дед?
        3 - Добавить пару(сын - отец).
        4 - Изменить пару(сын - отец).
        5 - Удалить пару(сын - отец).
        """
    )
    choice = int(input("Сделайте выбор: "))
    if choice == 1:
        son = input("Введи как тебя зовут: ")
        if son in familyTree:
            print("Твоего отца зовут", familyTree.get(son))
        else:
            print("Тебя нет в моем списке")
    elif choice == 2:
        son = input("Введи как тебя зовут: ")
        if son in familyTree:
            son = familyTree[son]
            if son in familyTree:
                print("Твоего деда зовут", familyTree.get(son))
            else:
                print("Твоего деда нет в моем списке")
        else:
            print("Тебя нет в моем списке")
    elif choice == 3:
        son = input("Введи как тебя зовут: ")
        if son not in familyTree:
            dad = input("Введи как зовут твоего отца: ")
            familyTree[son] = dad
            print("Пара успешно добавлена")
        else:
            print("Такая пара уже существует, попробуй изменить ее")
    elif choice == 4:
        son = input("Введи ключ пары которую ты хочешь изменить: ")
        if son in familyTree:
            dad = input("Введи на что ты хочешь изменить значение: ")
            familyTree[son] = dad
            print("Пара успешно изменена")
        else:
            print("Такой пары не существует, попробуй добавить ее")
    elif choice == 5:
        son = input("Введи ключ пары которую ты хочешь удалить: ")
        if son in familyTree:
            del familyTree[son]
            print("Пара успешно удалена")
        else:
            print("Такой пары не существует")
