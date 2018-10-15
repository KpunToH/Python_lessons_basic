# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
#Задача-1
def create_directory(name):
    path_dir = os.path.join(os.getcwd(), name)
    os.mkdir(path_dir)
def delete_directory(name):
    path_dir = os.path.join(os.getcwd(), name)
    os.rmdir(path_dir)
for i in range(1, 10): create_directory(f"dir_{i}")
for i in range(1, 10): delete_directory(f"dir_{i}")

#Задача-2
def change_directory(_):
    os.chdir(_)
def spisok():
    spisok = os.listdir(path=os.getcwd())
    print("Список файлов и папок в текущей директории:")
    for i in spisok:
        print(i)
change_directory("..")
spisok()

#Задача-3
import shutil
#Использую зарезервированную переменную  __file__, которая содержит имя python-скрипта
def copy_file():
    copy = __file__ + ".copy"
    shutil.copyfile(__file__, copy)
copy_file()