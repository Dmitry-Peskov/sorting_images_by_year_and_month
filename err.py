class ImagesNotFound(Exception):
    def __init__(self, value):
        """Исключение. В выбранной директории отсутствуют изображения"""
        super().__init__(f'[{self.__class__.__name__}] В выбранной директории "{value}" не было обнаружено изображений\n')

class FailedToBuildStructure(Exception):
    def __init__(self):
        """Исключение. Не удалось построить иерархию выходных каталогов"""
        super().__init__(f'[{self.__class__.__name__}] Не удалось создать дочерние каталоги в выходной директории.\nВозможно у изображений нет метаданных.\n')