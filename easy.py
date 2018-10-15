
#����-���������� ������� ��� ������� 5-������

import os

def create_directory(name):
    path_dir = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(path_dir)
        print(f"���������� {name} ������� �������")
    except FileExistsError:
        print(f"������ �������� - ���������� {name} ��� ����������")
def delete_dir(name):
    path_dir= os.path.join(os.getcwd(), name)
    try:
        os.rmdir(path_dir)
        print(f"���������� {name} ������� �������")
    except FileNotFoundError:
        print(f"������ - ���������� {name} ����������")
def change_dir(name):
    path_dir = os.path.join(os.getcwd(), name)
    try:
        os.chdir(path_dir)
        print(f"���������� {name} ������� �������")
    except FileNotFoundError:
        print(f"������ - ���������� {name} �� �������")
def show_content():
    spisok = os.listdir(path=os.getcwd())
    print("������ ��������� � ������� ����������:")
    for i in spisok:
        print(i)
