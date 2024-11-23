def merge_sort(arr):

    comparisons_count, initializations_count = merge_sort_and_count(arr, 0, len(arr) - 1)
    
    return comparisons_count, initializations_count


def merge_sort_and_count(arr, left, right):

    if left < right:
        mid = (left + right) // 2

        comparisons1, initializations1 = merge_sort_and_count(arr, left, mid)
        comparisons2, initializations2 = merge_sort_and_count(arr, mid + 1, right)
        comparisons3, initializations3 = merge_and_count(arr, left, mid, right)

        return comparisons1 + comparisons2 + comparisons3, initializations1 + initializations2 + initializations3

    return 0, 0


def merge_and_count(arr, left, mid, right):
    left_list = arr[left : mid + 1]
    right_list = arr[mid + 1 : right + 1]

    comparisons = initializations = i = j = 0

    while i < len(left_list) and j < len(right_list):
        comparisons += 1
        if left_list[i] <= right_list[j]:
            arr[left] = left_list[i]
            initializations += 1
            i += 1

        else:
            arr[left] = right_list[j]
            initializations += 1
            j += 1

        left += 1

    while i < len(left_list):
        arr[left] = left_list[i]
        i += 1
        left += 1
        initializations += 1
    
    return comparisons, initializations