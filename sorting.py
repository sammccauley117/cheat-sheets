from random import shuffle

# Double for loop looking for the max/min element on each iteration
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def selection(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr

# Recursively sort left and right side and then merge
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
def merge(arr):
    # The actual merge phase
    def _merge(left, right):
        sorted = [] # Result list

        # Merge two ordered lists
        while left and right:
            if left[0] < right[0]:
                sorted.append(left.pop(0))
            else:
                sorted.append(right.pop(0))

        # Add leftovers if the lists were different sizes
        if left:
            sorted += left
        if right:
            sorted += right

        return sorted

    # Base case: list is already broken down full
    # a list of 0 or 1 elements is already sorted
    count = len(arr)
    if count <= 1:
        return arr

    # Break up left and right sides
    left = arr[:count//2]
    right = arr[count//2:]

    # Sort the left and right sides independent
    left = merge(left)
    right = merge(right)

    # Merge the left and right sides
    return _merge(left, right)

x = [i for i in range(10)]
shuffle(x)
print('Unsorted: ', x)
print('Selection:', selection(x))
print('Merge:    ', merge(x))
print(x)
