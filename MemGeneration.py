from PIL import Image, ImageDraw, ImageFont
import random

print("Генератор мемов запущен!")

top_text = input("Введите верхний текст ")
bottom_text = input("Введите нижний текст ")

print("Список картинок:\nКот в очках - 1\nКот в ресторане - 2")

image_number = input("Введи номер картинки!")

if image_number == "1":
    image_file = "Кот в очках.png"
elif image_number == "2":
    image_file = "Кот в ресторане.png"

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=70)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height, - 10), bottom_text, font=font, fill="black")

random_name = random.randint(1, 500)
image.save(f"new_meme{random_name}.jpg")