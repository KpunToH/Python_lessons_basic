
#Мини-библиотека функций для задания 5-нормал

import os

def create_directory(name):
    path_dir = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(path_dir)
        print(f"Директория {name} успешно создана")
    except FileExistsError:
        print(f"Ошибка создания - директория {name} уже существует")
def delete_dir(name):
    path_dir= os.path.join(os.getcwd(), name)
    try:
        os.rmdir(path_dir)
        print(f"Директория {name} успешно удалена")
    except FileNotFoundError:
        print(f"Ошибка - директория {name} отсутсвует")
def change_dir(name):
    path_dir = os.path.join(os.getcwd(), name)
    try:
        os.chdir(path_dir)
        print(f"Директория {name} успешно выбрана")
    except FileNotFoundError:
        print(f"Ошибка - директория {name} не найдена")
def show_content():
    spisok = os.listdir(path=os.getcwd())
    print("Список элементов в текущей директории:")
    for i in spisok:
        print(i)
