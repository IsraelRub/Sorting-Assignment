import random

def quick_sort(arr):
        comparisons_count, initializations_count = quick_sort_and_count(arr, 0, len(arr) - 1)
        return comparisons_count, initializations_count

def quick_sort_and_count(arr, left, right):

    if left < right:
        smaller, larger, comparisons1, initializations1 = partition_and_count(arr, left, right)
        comparisons2, initializations2 = quick_sort_and_count(arr, left, smaller - 1)
        comparisons3, initializations3 = quick_sort_and_count(arr, larger + 1, right)

        return comparisons1 + comparisons2 + comparisons3, initializations1 + initializations2 + initializations3

    return 0, 0


def partition_and_count(arr, left, right):
    comparisons = initializations = 0

    rand = random.randint(left, right)
    arr[rand], arr[right] = arr[right], arr[rand]
    initializations += 2

    pivot = arr[right]

    low = i = left
    high = right

    while i <= high:
        comparisons += 1

        if arr[i] < pivot:
            arr[i], arr[low] = arr[low], arr[i]
            initializations += 2

            low += 1
            i += 1

        elif arr[i] > pivot:
            arr[i], arr[high] = arr[high], arr[i]
            initializations += 2
            high -= 1

        else:
            i += 1
    
    return low, high, comparisons, initializations