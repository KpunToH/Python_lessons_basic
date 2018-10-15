
#Мини-библиотека для нормал-5
import os

def create_directory(name):
    path_dir = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(path_dir)
        print(f"Директория {name} успешно создана")
    except FileExistsError:
        print(f"Директория {name} уже существует")
def delete_directory(name):
    path_dir= os.path.join(os.getcwd(), name)
    try:
        os.rmdir(path_dir)
        print(f"Директория{name} успешно удалена")
    except FileNotFoundError:
        print(f"Директория {name} отсутсвует")
def change_directory(name):
    path_dir = os.path.join(os.getcwd(), name)
    try:
        os.chdir(path_dir)
        print(f"Текущая директория{name} выбрана в качестве рабочей")
    except FileNotFoundError:
        print(f"Не найдена директория {name} ")
def spisok():
    spisok = os.listdir(path=os.getcwd())
    print("Список элементов текущей директории:")
    for i in spisok:
        print(i)
