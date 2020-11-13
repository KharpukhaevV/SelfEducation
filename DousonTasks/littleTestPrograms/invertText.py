print("Текст наоборот")
text = input("Введите текст который я инвертирую: ")
newText = ""
for i in range(len(text)-1, -1, -1):
    newText += text[i]
print("Вот что получилось: ", newText)
