from PIL import Image, ImageDraw, ImageFont
import os

# Папка, где находятся ваши изображения
image_folder = 'images'

# Папка, куда будут сохранены обработанные изображения
output_folder = 'edited-images'

# Проверьте, существует ли папка для выходных изображений; если нет, создайте её
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Список файлов в папке с изображениями
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

for image_file in image_files:
    # Открываем изображение
    with Image.open(os.path.join(image_folder, image_file)) as img:
        draw = ImageDraw.Draw(img)

        # Выбираем шрифт и размер
        font = ImageFont.truetype("OpenSans-Regular.ttf", 40)

        # Получаем название файла без расширения
        base_name = os.path.splitext(image_file)[0]

        # Получаем размеры текста
        text_width, text_height = draw.textsize(base_name, font=font)

        # Вычисляем позицию для текста, чтобы он был расположен внизу и по центру
        x = (img.width - text_width) / 2
        y = img.height - text_height - 100  # 20 - это отступ от нижнего края, его можно настроить

        # Сначала рисуем тень
        shadow_offset = (2, 2)  
        draw.text((x + shadow_offset[0], y + shadow_offset[1]), base_name, fill=(0,0,0), font=font)

        # Теперь рисуем основной текст красным цветом
        draw.text((x, y), base_name, fill=(255,0,0), font=font)

        # Сохраняем новое изображение в папку для выходных файлов
        img.save(os.path.join(output_folder, image_file))

print("All images processed.")
