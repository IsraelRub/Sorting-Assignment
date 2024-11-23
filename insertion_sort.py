def insertion_sort(arr):
    comparisons_count = initializations_count = 0

    for j in range(1 ,len(arr)):
        i = j - 1
        key = arr[j]

        while i >= 0 and arr[i] > key:
            comparisons_count += 1
            arr[i + 1] = arr[i]
            initializations_count += 1
            i -= 1

        if i != -1:
            comparisons_count += 1


        arr[i + 1] = key
        initializations_count += 1
    
    return comparisons_count, initializations_count