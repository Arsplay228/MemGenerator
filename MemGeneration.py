print("Генератор мемов запущен!")

top_text = input("Введите верхний текст")
bottom_text = input("Введите нижний текст")

print("Список картинок:\nКот в очках - 1\nКот в ресторане - 2")

number = input("Введи номер картинки!")

if number == "1":
    image = "Кот в очках.png"
elif number == "2":
    image = "Кот в ресторане.png"