import random

array = [i for i in range(10)]
random.shuffle(array)
print(array)

# 1 вариант
# n = 1
# while n < len(array):
#     min_value = array[n-1]
#     index = n - 1
#     for ind, value in enumerate(array[n-1:]):
#         if value < min_value:
#             min_value = value
#             index = n-1 + ind
#
#     array[n-1], array[index] = min_value, array[n-1]
#     n += 1
#
# print(array)

# 2 вариант
def select_sort(array):
    for i in range(len(array) - 1):
        for k in range(i + 1, len(array)):
            if array[k] < array[i]:
                array[k], array[i] = array[i], array[k]

select_sort(array)
print(array)