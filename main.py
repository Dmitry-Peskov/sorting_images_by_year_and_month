from obj import *

if __name__ == "__main__":
    while True:
        folder = WorkFolder()
        try:
            folder.define()  # определяем рабочую директорию
            folder.scan()  # ищем изображения в рабочей директории
        except ImagesNotFound as error:
            print(error)
            continue

        directory, images = folder.path, folder.images  # путь к рабочему каталогу и список путей к изображениям в нём.

        structure = StructureCreator(directory, images)
        try:
            structure.create()  # создаём в directory дочерние папки по годам / месяцам на основе данных из изображений
        except FailedToBuildStructure as error:
            print(error)
            continue

        routes = structure.routes # список маршрутов для копирования файлов
        Sorter.copy(routes=routes) # копируем файлы по заданным маршрутам
        Sorter.open_folder(directory) # открываем выходной каталог в проводник Windows
