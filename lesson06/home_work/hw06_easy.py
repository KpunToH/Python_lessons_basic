# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def side_lenght(self, point1, point2):
        #считаем длину каждой стороны
            side_lenght = abs(((point2[0] - point1[0]) ** 2 + ((point2[1] - point1[1]) ** 2)) ** 0.5)
            return side_lenght

    def storoni(self, A, B, C):
        #выполняем все требуемы расчеты
        AB = triangle.side_lenght(self, A, B)
        AC = triangle.side_lenght(self, A, C)
        BC = triangle.side_lenght(self, B, C)
        return AB, AC, BC


    def perimetr (self,A, B, C):
        # периметр
        AB, AC, BC =triangle.storoni(self, A, B, C)
        P = (AB + AC + BC)
        return P
    def ploshad (self,A, B, C):
        S = (0.5 * (abs((B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1]))))
        return S
    def visoti (self,A, B, C):
        #высоты треугольника
        S = triangle.ploshad(self, A, B, C)
        AB, AC, BC =triangle.storoni(self, A, B, C)
        AA1 = (2 * S) / BC
        BB1 = (2 * S) / AC
        CC1 = (2 * S) / AB
        return AA1, BB1, CC1

#Проверка
triangle1 = triangle((2,5),(3,7),(5,1))

print("Периметр треугольника равен " + str(triangle1.perimetr(triangle1.A, triangle1.B, triangle1.C)))
print("Площадь треугольника равна " + str(triangle1.ploshad(triangle1.A, triangle1.B, triangle1.C)))
print("Высоты треугольника равны " + str(triangle1.visoti(triangle1.A, triangle1.B, triangle1.C)))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

