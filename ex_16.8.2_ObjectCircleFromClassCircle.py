# Выполните задание, взяв за основу полученный код из задания 16.8.1. Добавьте еще один класс —
# круг (class Circle), который принимает в качестве аргументов свой радиус.
# Вычислите площадь круга

from ex_16_8_2_CreateClassCircle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(10, 15)
# print(rect_1.get_area(), rect_2.get_area()) # 12 150

square_1 = Square(5)
square_2 = Square(10)
# print(square_1.get_area_square(), square_2.get_area_square())   # 25 100

circle_1 = Circle(5)
circle_2 = Circle(10)
# print(circle_1.get_area_circle(), circle_2.get_area_circle())   # 78.5 314.0


figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Circle):
        print(figure.get_area_circle())
    elif isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())
