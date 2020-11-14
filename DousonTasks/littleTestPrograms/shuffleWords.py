import random

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
shuffleWords = []
while len(WORDS) != len(shuffleWords):
    newWord = random.choice(WORDS)
    if newWord not in shuffleWords:
        shuffleWords.append(newWord)
print("Заданные слова:\n", WORDS)
print("Перемешанные слова:\n", shuffleWords)
input("Нажмите Enter что бы выйти")
