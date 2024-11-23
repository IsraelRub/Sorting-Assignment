
def max_heapify(arr, i, heap_size):
    comparisons_count = initializations_count = 0
    left = i * 2 + 1
    right = i * 2 + 2

    largest = left if left < heap_size and arr[left] > arr[i] else i
    comparisons_count += 1

    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    comparisons_count += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        initializations_count += 2

        temp_comparisons, temp_initializations = max_heapify(arr, largest, heap_size)
        comparisons_count += temp_comparisons ; initializations_count += temp_initializations
    
    return comparisons_count, initializations_count


def build_max_heap(arr):
    comparisons_count = initializations_count = 0
    heap_size = len(arr)

    for i in range((len(arr) // 2) - 1, -1, -1):
        temp_comparisons, temp_initializations = max_heapify(arr, i, heap_size)
        comparisons_count += temp_comparisons ; initializations_count += temp_initializations
    
    return comparisons_count, initializations_count


def heap_sort(arr):
    comparisons_count, initializations_count = build_max_heap(arr)
    heap_size = len(arr)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        initializations_count += 2

        heap_size -= 1
        temp_comparisons, temp_initializations = max_heapify(arr, 0, heap_size)
        comparisons_count += temp_comparisons ; initializations_count += temp_initializations
    
    return comparisons_count, initializations_count  