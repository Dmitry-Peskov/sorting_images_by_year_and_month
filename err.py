class ImagesNotFound(Exception):
    def __init__(self, value):
        """Исключение. В выбранной директории отсутствуют изображения"""
        super().__init__(f'[{self.__class__.__name__}] В выбранной директории "{value}" не было обнаружено изображений')
