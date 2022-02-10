import random


def hoara_sort(array):
    if len(array) <= 1:
        return array

    small = []
    large = []
    pivot = random.choice(array)

    for item in array:
        if item < pivot:
            small.append(item)
        else:
            large.append(item)
    print(small, large)
    return hoara_sort(small) + hoara_sort(large)


# array = [9, 6, 3, 4, 10, 8, 2, 7]
# print(hoara_sort(array))


def quick_sort_no_memory(array, first, last):
    if first >= last:
        return

    print(array, first, last)

    pivot = array[random.randint(first, last)]
    print(pivot)
    i, j = first, last

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            print('change = ', array[i], array[j] )
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

        quick_sort_no_memory(array, first, j)
        quick_sort_no_memory(array, i, last)



array = [9, 6, 3, 4, 10, 8, 2, 7]
print(quick_sort_no_memory(array, 0, len(array) -1 ))