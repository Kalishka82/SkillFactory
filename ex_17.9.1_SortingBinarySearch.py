# Напишите программу, которой на вход подается последовательность
# чисел через пробел, а также запрашивается у пользователя любое число.
#
# В качестве задания повышенного уровня сложности можете выполнить
# проверку соответствия указанному в условии ввода данных.
#
# Далее программа работает по следующему алгоритму:
# 1. Преобразование введённой последовательности в список
# 2. Сортировка списка по возрастанию элементов в нем (для
# реализации сортировки определите функцию)
# 3. Устанавливается номер позиции элемента, который меньше
# введенного пользователем числа, а следующий за ним больше или равен этому числу.

# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска,
# который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
import random

strInp = input("Input some integer numbers through the space: ")
# list_ = [random.randint(0, 100) for i in range(10)]     # другой возможный вариант
# сразу задать массив из рандомных чисел, использовался для проверки работы
# алгоритма, чтобы каждый раз не задавать числа вручную
array = list(map(int, strInp.split()))
numToFind = int(input("Input any integer number: "))


# def sort1_list(array):  # сортировка выбором
#     for i in range(len(array)):
#         idx_min = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[idx_min]:
#                 idx_min = j
#         if i != idx_min:
#             array[i], array[idx_min] = array[idx_min], array[i]
#     return array
#
#
# print(sort1_list(array))
#
# array = list(map(int, strInp.split()))
# print(array)


def sort2_list(array):  # сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(sort2_list(array))


def binary_search(array, numToFind, left, right):
    if left > right:
        return False
    middle = (right + left) // 2

    if array[middle] < numToFind and array[middle + 1] >= numToFind:
        return middle
    elif numToFind < array[middle]:
        return binary_search(array, numToFind, left, middle - 1)
    else:
        return binary_search(array, numToFind, middle + 1, right)


if array[0] < numToFind <= array[len(array) - 1]:
    print(f'Element Position of numToFind is {binary_search(array, numToFind, 0, len(array) - 1)}')
else:
    print("There is no such number in the list")
