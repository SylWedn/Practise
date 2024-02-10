def binary_search_recursive(arr, target, low, high):
    # Base case: if the lower index exceeds the upper index, the element is not found
    if low > high:
        return -1

    # Find the middle index
    mid = (low + high) // 2

    # If the value at the middle index is equal to the target, return the index
    if arr[mid] == target:
        return mid
    # If the value at the middle index is greater than the target, recursively search in the left half of the array
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    # If the value at the middle index is less than the target, recursively search in the right half of the array
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")
