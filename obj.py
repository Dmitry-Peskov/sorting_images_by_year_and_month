import os
import shutil
from datetime import datetime
from err import *

FILE_EXTENSION = ('.bmp', '.gif', '.jpeg', '.ico', '.png', '.jfif', '.heic', '.jpg')


class WorkFolder:
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
                    self.__path = path if path[-1] != '\\' else path[0:len(path) - 1]
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


class StructureCreator:
    def __init__(self, directory: str, images: list[str]):
        self.__dir = directory
        self.__imgs = images
        self.__output = self.__create_output_folder()
        self.__routes = dict()

    @property
    def routes(self) -> dict[str, str]:
        return self.__routes

    def __create_output_folder(self) -> str:
        path = self.__dir + "\\Изображения"
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def create(self):
        for image in self.__imgs:
            dt = datetime.fromtimestamp(os.path.getmtime(image))
            if dt is None:
                print(f'Для изображения "{image}" не удалось определить дату/время создания')
                continue
            else:
                year = f'{self.__output}\\{dt.year}'
                month = f'{year}\\{dt.month}'
                if not os.path.exists(year):
                    os.mkdir(year)
                if not os.path.exists(month):
                    os.mkdir(month)
                self.__routes[image] = month
        cnt_routes = len(self.__routes)
        if cnt_routes == 0:
            raise FailedToBuildStructure()
        else:
            print(f'Построено {cnt_routes} маршрутов для копирования')


class Sorter:

    @staticmethod
    def copy(routes: dict[str, str]):
        for image, output in routes.items():
            file_name = image.split('\\')[-1]
            new_file = f'{output}\\{file_name}'
            shutil.copy2(src=image, dst=new_file, follow_symlinks=True)
            print(f'Файл {file_name} скопирован в "{output}"')

    @staticmethod
    def open_folder(path: str):
        path = os.path.realpath(path)
        os.startfile(path)
