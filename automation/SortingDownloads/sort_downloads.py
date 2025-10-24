import hashlib
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog,QMessageBox, QErrorMessage
from pathlib import Path

# #class filemanager
file_type_categories = {
    'jpeg': 'Зображення', 'jpg': 'Зображення', 'png': 'Зображення',
    'gif': 'Зображення', 'svg': 'Зображення', 'bmp': 'Зображення',
    'ico': 'Зображення', 'tiff': 'Зображення', 'webp': 'Зображення',
    'heic': 'Зображення', 'raw': 'Зображення',
    'mp4': 'Відео', 'mov': 'Відео', 'avi': 'Відео', 'mkv': 'Відео',
    'wmv': 'Відео', 'flv': 'Відео', 'webm': 'Відео', 'mpeg': 'Відео',
    'mp3': 'Аудіо', 'ogg': 'Аудіо', 'wav': 'Аудіо', 'flac': 'Аудіо',
    'aac': 'Аудіо', 'm4a': 'Аудіо',
    'doc': 'Документи', 'docx': 'Документи', 'pdf': 'Документи',
    'txt': 'Документи', 'rtf': 'Документи', 'odt': 'Документи',
    'md': 'Документи',
    'xls': 'Таблиці', 'xlsx': 'Таблиці', 'csv': 'Таблиці',
    'ods': 'Таблиці',
    'ppt': 'Презентації', 'pptx': 'Презентації', 'key': 'Презентації',
    'odp': 'Презентації',
    'zip': 'Архіви', 'rar': 'Архіви', '7z': 'Архіви', 'tar': 'Архіви',
    'gz': 'Архіви', 'bz2': 'Архіви', 'iso': 'Образи дисків',
    'exe': 'Файли виконання', 'msi': 'Інсталятори', 'bat': 'Скрипти',
    'sh': 'Скрипти', 'dll': 'Системні файли', 'jar': 'Файли виконання',
    'py': 'Код Python', 'js': 'Код JavaScript', 'html': 'Веб-сторінки',
    'css': 'Стилі', 'json': 'Дані', 'xml': 'Дані', 'sql': 'Код SQL',
    'java': 'Код Java', 'c': 'Код C', 'cpp': 'Код C++', 'cs': 'Код C#',
    'php': 'Код PHP', 'rb': 'Код Ruby',
    'psd': 'Проєкти Photoshop', 'ai': 'Проєкти Illustrator',
    'fig': 'Проєкти Figma', 'sketch': 'Проєкти Sketch',
    'obj': '3D Моделі', 'fbx': '3D Моделі', 'blend': 'Проєкти Blender',
    'ttf': 'Шрифти', 'otf': 'Шрифти', 'woff': 'Шрифти', 'woff2': 'Шрифти',
    'torrent': 'Торренти', 'log': 'Лог-файли', 'bak': 'Резервні копії'
}
#
app = QApplication([])
window = QWidget()
window.setWindowTitle('FirstApp')
error_dialog = QErrorMessage()
error_dialog.setWindowTitle('Помилка!')
dir_path = QFileDialog.getExistingDirectoryUrl()

if dir_path:
    path = dir_path.path()[1:]#бо слеш на початку

data = os.listdir(path) #всі файли теки
data_and_ext = {} #назви файлів і розширення
fold_to_create = set() #папки що потрібно стоврити
created_dirs = [] #вже створені папки
items_to_transfer = []
folders_for_transfer = []

#отримуємо список всіх потрібних розширень для створення



def get_ext():
    global data_and_ext
    for x in data:
        print(x)
        if '.' not in x:
            continue
        extension = x.split('.')[-1] #extension
        items_to_transfer.append(x)
        if extension in data_and_ext:
            data_and_ext[extension].append(x)
        else:
            data_and_ext[extension] = [x]
    print(data_and_ext)



def get_folders_to_create_and_transfer():
    global fold_to_create, folders_for_transfer
    for key, value in data_and_ext.items():
        fold_to_create.update({file_type_categories.get(key)})

    for folder in fold_to_create:
        folders_for_transfer.append(folder)


    #видаляємо папки для створення якщо вони вже є в завантаженнях
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir() and entry.name in fold_to_create and entry.name.split('_')[0] in fold_to_create:
                    created_dirs.append(entry.name)
                    fold_to_create.remove(entry.name)
    except KeyError:
        pass
    except FileNotFoundError:
        print(f"ПОМИЛКА: Папку '{path}' не знайдено!")
    except Exception as e:
        print(f"Сталася невідома помилка: {e}")


#створюємо папки, якщо їх немає
def creating_folders(path1):
    try:
        if fold_to_create:
            for folder in fold_to_create:
                os.mkdir(f'{path1}/{folder}')
    except FileExistsError:
        pass

print(data_and_ext)
def transfer_files(path1):
    global data_and_ext
    try:
        for extens, files in data_and_ext.items():
            print(extens)
            fold = file_type_categories.get(extens)
            for file in files:
                pass
                # print(f'{path1}/{file}',f'{path1}/{fold}/{file}')
                # os.rename(f'{path1}/{file}',f'{path1}/{fold}/{file}')
    except FileNotFoundError:
        pass


get_ext()
get_folders_to_create_and_transfer()
creating_folders(path)
transfer_files(path) # тут помилка

#
#
# #РЕАЛІЗАЦІЯ ПАПОК
# if dir_path:
#     path = dir_path.path()[1:]#бо слеш на початку
#
#
# #потрібно отримати назви усіх папок по яким ітеруватися
# size = 0
# dirs = []
#
#
# #отримуємо список папок по шляху
# for file in os.scandir(path):#бо слеш на початку
#     if file.is_dir():
#         dirs.append(file.name)
#
#
# #отримуємо список папок що потрібно буде проаналізувати (з врахуванням формату "dir_2.5gb")
# new_dirs = []
# for y in dirs:
#     if y in file_type_categories.values() or y.split('_')[0] in file_type_categories.values():
#         new_dirs.append(y)
#
#
# #отримуємо розмір папки
# def get_size(start_path = '.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             if not os.path.islink(fp):
#                 total_size += os.path.getsize(fp)
#     if total_size:
#         if 0 > total_size > 125:
#             return f"{total_size / 1024:.2f}" + 'B'
#         elif 1048576 > total_size > 125:
#             return f"{total_size/1024:.2f}" + 'KB'
#
#         elif 1073741824 > total_size > 1048576:
#             return f"{total_size / 1048576:.2f}" + 'MB'
#
#         elif 1099511627776 > total_size > 1073741824:
#             return f"{total_size / 1073741824:.2f}" + 'GB'
#         else:
#             return f"{total_size / pow(1024, 4):.2f}" + 'TB'
#     else:
#         return 0
#
# try:
#     if dirs:
#         #ітерація по папкам для перейменування
#         for x in dirs:
#             p = str(path)+"/"+x
#             size = get_size(p)
#             if "_" in p:
#                 os.rename(p, p.split('_')[0] + "_" + size)
#             else:
#                 os.rename(p, p + "_" + size)
# except FileExistsError:
#     error_dialog.showMessage(f'Файли мають однакові назви')
#     app.exec()
