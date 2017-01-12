# Image Resizer

Скрипт-ресайзер изображений -  принимает на вход изображение и кладёт изображение с новым размером
куда скажет пользователь или рядом с исходным. 
Параметры :
* Обязательный аргумент - путь до исходной картинки. 

* Необязательные: 

`-w, --width` — ширина результирующего изображения

`-ht, --height` — высота результирующего изображения

`-s, --scale`  — во сколько раз увеличить изображение (может быть меньше 1)

`-o, --output` - куда класть результирующий файл 
(если не указан, сохраняется рядом с исходным файлом ).

# Зависимости

    pip3 install -r requirements.txt

# Запуск скрипта

Пример запуска скрипта:

    python3.5 image_resize.py file [--scale --width  --height --output ]


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
