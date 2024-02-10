def count_elements(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: return 1 (for the current element) plus
    # the count of elements in the list starting from the next element
    return 1 + count_elements(lst[1:])

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Number of elements in the list:", count_elements(my_list))
