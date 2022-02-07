import random

# array = [i for i in range(10)]
# random.shuffle(array)
# print(array)

# def insertion_sort(array):
#     for i in range(1, len(array)):
#         value = array[i]
#         index = i
#
#         while value < array[index-1] and index != 0:
#             array[index] = array[index - 1]
#             index -= 1
#
#         array[index] = value
#
# def shell_sort(array):
#     steps = [5, 3, 1]
#
#     for step in steps:
#         array2 = []
#         for i in range(step):
#             array2.append(array[i::step])
#
#         for i in array2:
#             insertion_sort(i)
#             print('array2 =',  array2)
#
#     return array2




def shell_sort2(array):
    def new_increment(array):
        # inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        inc = [1, 3, 5]
        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            # print('i = ', i)
            for j in range(i, increment - 1, -increment):
                # print('j = ', j)
                if array[j - increment] <= array[j]:
                    # print('break = ', array[j - increment], array[j] )
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                print(array)



array = [32, 95, 16, 82, 24, 66, 35,19, 75, 54, 40, 43, 93, 68]
# array = shell_sort(array)
shell_sort2(array)
print(array)