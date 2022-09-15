# Создать класс SquareException. Добавить в конструктор класса
# Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать
# каждый раз, когда сторона квадрата меньше или равна 0.

class NonPosititveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        self.a = a
        if a <= 0:
            raise NonPosititveDigitException('Неправильно указана сторона квадрата')

    def get_area(self):
        return self.a ** 2


square_1 = Square(5)
square_2 = Square(10)
square_3 = Square(8)

square_list = [square_1.get_area(), square_2.get_area(), square_3.get_area()]
print(square_list)  # [25, 100, 64]

square_4 = Square(-8)   # Неправильно указана сторона квадрата
square_list_1 = [square_3.get_area(), square_4.get_area()]
print(square_list_1)

