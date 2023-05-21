## Сортировка изображений по папкам "год" и "месяц"

Утилита производит сортировку изображений в выбранном каталоге по папкам соответствующим году и месяцу создания изображения.

### Доступные расширения изображений:
> bmp, gif, jpeg, ico, png, jfif, heic, jpg  


### Алгоритм работы: 
1. Пользователь указывает путь к каталогу с изображениями
2. Утилита проверяет существование изображений в выбранном каталоге.  
   **Изображений нет** - вызывается исключение и происходит перезапуск выполнения утилиты  
   **Изображения есть** - выполнение программы продолжается
3. В выбранном каталоге создается директория *"Изображения"*
4. Для каждого обнаруженного в корневом каталоге изображения определяется *год* и *месяц* его создания
4.1. Если в папке *"Изображения"* ещё не существует путь *"\год\месяц"* - производиться его создания 
5. Происходит перемещение изображений из корневого каталога в подкаталог *"Изображения\год\месяц"*

### Пример:
Мы имеем каталог *"D:"* с содержимым: 
- D:  
  - 20210212_23423.jpg
  - 20210212_21343.jpg
  - 20211212_234.jpg
  - 20211212_221.jpg
  - 20230730_24353.jpg
  - 20230705_24353.jpg

После выполнения программы для каталога *"D:" мы получим:*
- D:
  - Изображения  
    - 2021  
      - 2  
        - 20210212_23423.jpg
        - 20210212_21343.jpg
      - 12  
        - 20211212_234.jpg
        - 20211212_221.jpg
    - 2023  
      - 7  
        - 20230730_24353.jpg
        - 20230705_24353.jpg



    


