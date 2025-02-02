import random

# Partition function (Lomuto's partition scheme)
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
    return i + 1  # Return the partition index

# Randomized partition function
def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)  # Choose a random pivot
    arr[rand_index], arr[high] = arr[high], arr[rand_index]  # Swap with last element
    return partition(arr, low, high)

# Randomized Quicksort function
def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)  # Get partition index
        randomized_quicksort(arr, low, pi - 1)  # Recursively sort left subarray
        randomized_quicksort(arr, pi + 1, high)  # Recursively sort right subarray

# Example usage
arr = [10, 7, 8, 9, 1, 5]
randomized_quicksort(arr, 0, len(arr) - 1)
print("Randomized Sorted array:", arr)