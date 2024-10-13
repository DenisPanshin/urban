import os
import time

directory = r'C:\Users\admin\Downloads'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root)
        filetime = os.path.getmtime(root + '/' + file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(root + '/' + file)
        parent_dir = os.path.dirname(root)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
