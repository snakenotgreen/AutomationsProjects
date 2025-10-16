import hashlib
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog

#class filemanager
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

app = QApplication([])
window = QWidget()
window.setWindowTitle('FirstApp')
file = QFileDialog()
fileName, _ = QFileDialog.getOpenFileName(parent=window)
if fileName:
    path = os.path.dirname(fileName)

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
        if '.' not in x:
            continue
        extension = x.split('.')[-1] #extension
        items_to_transfer.append(x)
        if extension in data_and_ext:
            data_and_ext[extension].append(x)
        else:
            data_and_ext[extension] = [x]

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
                if entry.is_dir() and entry.name in fold_to_create:
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

def transfer_files(path1):
    try:
        for extens, files in data_and_ext.items():
            fold = file_type_categories.get(extens)
            for file in files:
                os.rename(f'{path1}/{file}',f'{path1}/{fold}/{file}')
    except FileNotFoundError:
        pass


get_ext()
get_folders_to_create_and_transfer()
creating_folders(path)
transfer_files(path)


