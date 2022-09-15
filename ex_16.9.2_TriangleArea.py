# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода init(). На выходе в консоли вам необходимо
# получить площадь данной фигуры.
# !!! выполнено на примере треугольника!!!

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Triangle: {self.a}, {self.b}, {self.c}"

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area_triangle(self):
        return ((self.get_perimeter() / 2 *
                 (self.get_perimeter() / 2 - self.a) *
                 (self.get_perimeter() / 2 - self.b) *
                 (self.get_perimeter() / 2 - self.c)) ** 0.5)


triangle_1 = Triangle(3, 4, 5)
print(triangle_1)                           # Triangle: 3, 4, 5
print(triangle_1.get_perimeter())           # 12
print(triangle_1.get_area_triangle())       # 6.0
