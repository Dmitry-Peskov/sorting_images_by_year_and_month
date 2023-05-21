import os
import shutil
from obj import *

folder = WorkingFolder()

if __name__ == "__main__":
    while True:
        try:
            folder.define() # выбираем рабочую директорию
            folder.scan() # ищем изображения в рабочем каталоге
        except ImagesNotFound as error:
            print(error)
            continue






