import random

array = [i for i in range(10)]
random.shuffle(array)
print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        index = i

        while value < array[index-1] and index != 0:
            array[index] = array[index - 1]
            index -= 1

        array[index] = value

insertion_sort(array)
print(array)