import os
from err import *

FILE_EXTENSION = ('.bmp','.gif','.jpeg','.ico','.png','.jfif','.heic','.jpg')

class WorkingFolder:
    def __init__(self):
        """
        Рабочая директория
        """
        self.__path: str = str(os.getcwd())
        self.__images: list[str] = list()

    @property
    def path(self):
        """Путь к директории с изображениями"""
        return self.__path

    @property
    def images(self):
        """Список путей к изображениям"""
        return self.__images

    def define(self) -> None:
        """
        Выбрать путь до рабочей директории

        :return: None
        """
        getcwd = str(os.getcwd())
        while True:
            command = str(input(f'Изображения для сортировки находяться здесь "{getcwd}" (y / n)?: ')).lower()
            if command == "y":
                self.__path = getcwd
                break
            elif command == 'n':
                path = str(input('Укажите путь к каталогу с изображениями: '))
                if os.path.exists(path):
                    self.__path = path if path[-1] != '\\' else path[0:len(path)-1]
                    break
                else:
                    print(f'Каталог "{path}" не существует. Попробуйте выбрать другой\n')
                    continue
            else:
                print(f'[Ошибка] Не допустимая команда "{command}". Ожидалось "y" или "n"\n')
                continue

    def scan(self) -> None:
        """
        Сканировать директорию на наличие изображений

        :return: None
        """
        for file in os.scandir(self.path):
            if file.is_file():
                for exstension in FILE_EXTENSION:
                    if file.name.endswith(exstension):
                        self.__images.append(file.path)
        cnt_images = len(self.images)
        if cnt_images != 0:
            print(f'В директории {self.path} обнаружено {cnt_images} изображений')
        else:
            raise ImagesNotFound(self.path)









