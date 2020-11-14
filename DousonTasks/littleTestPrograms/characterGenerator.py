statPoints = 30
stats = {"здоровье": 5, "сила": 2, "ловкость": 2, "интелект": 2}
print(
    """
            Добро пожаловать в генератор персонажей!
          Распределите характеристики вашего персонажа.
    """
)
choice = None
while choice != 0:
    print(
        """
            Доступно очков характеристик {0}
                Текущие характеристики:
        Здоровье {1}, Сила {2}, Ловкость {3}, Интелект {4}.
        0. Выйти
        1. Добавить характеристики
        2. Убавить характеристики
        """.format(statPoints, stats.get("здоровье"), stats.get("сила"), stats.get("ловкость"), stats.get("интелект"))
    )
    choice = int(input("\nВыберете пункт меню: "))
    if choice == 1:
        getKey = input("Введите характеристику: ")
        getKey = getKey.lower()
        while getKey not in stats:
            print("Такой характеристики не существует")
            getKey = input("Введите характеристику: ")
        if getKey in stats:
            getValue = int(input("Введите сколько добавить к {} :".format(getKey)))
            stats[getKey] += getValue
            statPoints -= getValue
    elif choice == 2:
        getKey = input("Введите характеристику: ")
        getKey = getKey.lower()
        while getKey not in stats:
            print("Такой характеристики не существует")
            getKey = input("Введите характеристику: ")
        if getKey in stats:
            getValue = int(input("Введите сколько убавить у {} :".format(getKey)))
            stats[getKey] -= getValue
            statPoints += getValue
