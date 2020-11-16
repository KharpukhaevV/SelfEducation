# Викторина
# Игра на выбор правильного варианта ответа.
# вопросы который читаются из текстового файла
import sys
import shelve


def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode, encoding="utf-8")
    except IOError as e:
        print("Невозможно открыть файл", file_name, ", Работа программы будет завершена.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    category = next_line(the_file)
    question = next_line(the_file)
    denomination = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, denomination, answers, correct, explanation


def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")


def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # извлечение первого блока
    category, question, denomination, answers, correct, explanation = next_block(trivia_file)
    player_name = input("Введите свое имя: ")
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # проверка ответа
        answer = input("Ваш ответ: ")
        if answer == correct:
            print("\nДа!", end=" ")
            score += int(denomination)
        else:
            print("\nНет,", end=" ")
        print(explanation)
        print("Счет:", score, "\n\n")
        # переход к следующему вопросу
        category, question, denomination, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашем счету", score)

    print("\n\nТаблица рекордов: ")
    rating_board = shelve.open("rating_board.dat")
    rating_board[player_name] = score
    rating_board.sync()
    for player in rating_board:
        print(player, rating_board[player])
    rating_board.close()

    print("\n\nТаблица рекордов_2: ")
    rating_board = open("rating_board2.txt", "a+", encoding='utf-8')
    rating = "{0} - {1}\n".format(player_name, score)
    rating_board.write(rating)
    for line in rating_board:
        print(line)
    rating_board.close()


main()
input("\n\nНажмите Enter, что бы выйти")
