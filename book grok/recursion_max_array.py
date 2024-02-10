def recursive_max(lst):
    # Base case: if the list is empty, return None
    if not lst:
        return None
    # Base case: if the list contains only one element, return that element
    if len(lst) == 1:
        return lst[0]
    # Recursive case: return the maximum value between the first element
    # and the maximum value of the rest of the list
    return max(lst[0], recursive_max(lst[1:]))

# Example usage:
my_list = [1, 5, 3, 9, 2, 7]
print("Maximum value in the list:", recursive_max(my_list))
