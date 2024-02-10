
def recursive_sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + recursive_sum(array[1:])


my_array = [1, 2, 3, 4, 5]
print("sum of all elements using recursive:", recursive_sum(my_array))