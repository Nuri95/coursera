import random


"""
    1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
    заданный случайными числами на промежутке [-100; 100).
    Выведите на экран исходный и отсортированный массивы.
"""

array = [i for i in range(-100, 100)]
random.shuffle(array)
# print(array)


def bubble_sort(array):
    count = 1
    while count < len(array):
        for i in range(len(array)-count):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        count += 1


# bubble_sort(array)
# print(array)


"""
    2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
    заданный случайными числами на промежутке [0; 50).
    Выведите на экран исходный и отсортированный массивы.
"""
# https://idroo.com/board-SFilaTFHpa - блок схема

array = [i for i in range(50)]
random.shuffle(array)
print(array)


def merge(array, left, right):
    # ar3 = []
    i, j = 0, 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            # ar3.append(left[i])
            array[i + j] = left[i]
            i += 1
        # elif left[i] > right[j]:
        else:
            # ar3.append(right[j])
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        # ar3.append(left[i])
        array[i + j] = left[i]
        i += 1

    while len(right) > j:
        # ar3.append(right[j])
        array[i + j] = right[j]
        j += 1


    return array


def merge_sort(array):
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    divide = len(array) // 2

    left = merge_sort(array[:divide])
    right = merge_sort(array[divide:])
    print(left, right)
    return merge(array, left, right)


array = [6, 5, 3, 1, 8, 7, 2, 4]
print(merge_sort(array))


"""
    3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
    Найдите в массиве медиану. 
    Медианой называется элемент ряда, делящий его на две равные части:
    в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

def shaker_sort(array):
    array_length = len(array)


def median():
    pass

array = [6, 4, 3, 2, 1, 4]
data = [random.randrange(0, 50) for _ in range(2 * 4 + 1)]
print(data)