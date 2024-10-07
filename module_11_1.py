import requests
from PIL import Image, ImageFilter


images = []  # Список для сохраненных изображений

class DownloadImage:  # Класс для скачивания изображений
    def __init__(self):
        self.image_count = 1

    def save_image(self, image_url):
        try:
            img = requests.get(image_url)
            file_name = f'img_{self.image_count}.png'
            with open(file_name, 'wb') as file:
                file.write(img.content)  # Сохраняеться изображение
                print(f'Скачали и сохранили {file_name}')
            self.image_count += 1
            images.append(file_name)  # Добавляем названия файла в список, для дальнейшей работы с ним
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при загрузке изображения: {e}')


class Editor:  # Класс который изменяет размер и тип изображений, а так применяет эффект размытия
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def resize_image(self, image_path):  # Метод изменяет размера изображения
        try:
            image = Image.open(image_path)
            current_width, current_height = image.size
            if current_width != self.width or current_height != self.height: # Проверка на соответствие размера изоб-я
                image = image.resize((self.width, self.height))
                image.save(image_path)
                print(f'Изображение {image_path} изменили размер на {self.width}x{self.height}')
        except FileNotFoundError:
            print(f'Файл {image_path} не найден')

    def blur(self, img_path, rad):  # Метод применяет размытие к изображению, а так же меняет тип файла
                                    # Размытие указываеться в аргументе rad
        try:
            image = Image.open(img_path)
            blurred_image = image.filter(ImageFilter.GaussianBlur(radius=rad)) # Размытие по Гауссу
            blurred_image.save(f'{img_path.split('.')[0]}_blur.jpg') # Переименовывание изображение
            print(f'К изображению {img_path} применена степень размытия {rad}')
        except FileNotFoundError:
            print(f'Ошибка: Файл {img_path} не найден')


# Обьявляеться список с ссылоками на изображений
list_url = ['https://hdwallsbox.com/wallpapers/l/1920x1080/79/animals-cars-glasses-outer-space-stars-1920x1080-'
            '78138.jpg',
            'https://get.wallhere.com/photo/sunlight-trees-forest-branch-morning-cherry-blossom-pink-tree-autumn-'
            'leaf-flower-plant-season-710182.jpg',
            'https://images.wallpaperscraft.ru/image/single/makro_rozovyj_roza_4537_1920x1080.jpg',
            'https://images.wallpaperscraft.ru/image/single/bozhia_korovka_kapli_poverhnost_106249_1920x1080.jpg']
downloader = DownloadImage()
save = [downloader.save_image(u) for u in list_url] # Проходиться по list_url и скачивает изображения

edit = Editor(1280, 720) # Указывается нужный размер изображений
resize = [edit.resize_image(img) for img in images] # изменяет размер скачанных изображений
blured = [edit.blur(img, 10) for img in images] # размывает все изображения с указанной степенью размытия {rad}

