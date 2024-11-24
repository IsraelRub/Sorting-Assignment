import random
import matplotlib.pyplot as plt
from typing import Tuple, Callable ,List, Dict

from merge_sort import merge_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort


sorting_algorithms: Dict[str, Callable[[List[int]], Tuple[int, int]]] = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Insertion Sort": insertion_sort,
    "Heap Sort": heap_sort
}


dict_of_list_types: Dict[str, Callable[[int], List[int]]] = {
    "Sorted": lambda size: list(range(size + 1)),
    "Reverse Sorted": lambda size: list(range(size, -1, -1)),
    "Equal Numbers": lambda size: [1234.567] * size,
    "Random Integers (With Duplicates)": lambda size: [random.randint(-int(size * 0.4), int(size * 0.4)) for _ in range(size)],
    "Random Floats (Unique Likely)": lambda size: [random.uniform(-size, size) for _ in range(size)]
}



def test_single_sorting_on_list_types(sort_name: str, list_size: int) -> None:
    
    # Test the specified sorting algorithm on different list types.


    for list_type, test_list in dict_of_list_types.items():
        print(f"\nTesting '{sort_name}' on '{list_type}' list with size {list_size}:")

        # Generate the list
        test_list = dict_of_list_types[list_type](list_size)

        # Sort using the selected algorithm
        sort_func = sorting_algorithms[sort_name]
        arr_copy = test_list.copy()
        comparisons, initializations = sort_func(arr_copy)
        total_operations = comparisons + initializations
        sorted_correctly = arr_copy == sorted(test_list)

        # Print the results
        print(f"Results for '{sort_name}':")
        print(f"  - Sorted Correctly: {sorted_correctly}")
        print(f"  - Comparisons: {comparisons}")
        print(f"  - Initializations: {initializations}")
        print(f"  - Total Operations: {total_operations}")



def test_sorting_algorithms_with_graphs(size: int, metric: str = "total") -> None:

    # Test the sorting algorithms with graphical performance analysis.

    figure, graphs = plt.subplots(nrows=2, ncols=(len(dict_of_list_types) + 1) // 2, figsize=(10, 6))
    figure.canvas.manager.set_window_title("Sorting Assignment")
    figure.suptitle(f"Performance Analysis: {metric.capitalize()} Operations", fontsize=16)

    graphs = graphs.flatten()

    for index, (list_type, numbers_list) in enumerate(dict_of_list_types.items()):
        comps_and_inits = {sort: [] for sort in sorting_algorithms.keys()}
        list_lengths = []

        for i in range(size // 10, size + 1, size // 10):
            random_list = numbers_list(i)
            list_lengths.append(len(random_list))

            for sort_name, sort_func in sorting_algorithms.items():
                result = sort_func(random_list.copy())
                match metric:
                    case "comparison":
                        comps_and_inits[sort_name].append(result[0])
                    case "initialization":
                        comps_and_inits[sort_name].append(result[1])
                    case "total":
                        comps_and_inits[sort_name].append(sum(result))
                    case _:
                        print("Metric must be one of 'comparisons', 'initializations', or 'totals'")
                        break

        current_graph = graphs[index]
        for sort_name, values in comps_and_inits.items():
            current_graph.plot(list_lengths, values, label=sort_name)
        
        current_graph.set_title(list_type)
        current_graph.set_xlabel("Length of List")
        current_graph.set_ylabel(f"{metric.capitalize()} Operations")
        current_graph.legend()
        current_graph.grid(True)

    for index in range(len(dict_of_list_types), len(graphs)):
        figure.delaxes(graphs[index])

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)
    plt.show()



def test_sorting_algorithms_with_prints(list_size: int) -> None:

    # Test sorting algorithms on predefined test cases and print results.

    for list_type in dict_of_list_types.keys():
        print(f"\nTesting all sorting on '{list_type}' list with size {list_size}:")

        # Generate the list
        test_list = dict_of_list_types[list_type](list_size)
        
        results = []
        for name, sort_func in sorting_algorithms.items():
            arr_copy = test_list.copy()
            comparisons, initializations = sort_func(arr_copy)
            total = comparisons + initializations
            sorted_correctly = arr_copy == sorted(test_list)
            results.append((name, comparisons, initializations, total, sorted_correctly))
        
        best_result = min(results, key=lambda x: x[3])
        print(f"\n  - Most efficient sorting: {best_result[0]}\n")
        
        for name, comparisons, initializations, total, sorted_correctly in results:
            print(f"    - {name}: Sorted: {sorted_correctly}, Comparisons: {comparisons}, Initializations: {initializations}, Total Operations : {total}")


def main() -> None:

    metric = "comparison"
    metric = "initialization"
    metric = "total"

    sort_name = "Quick Sort"
    sort_name = "Merge Sort"
    sort_name = "Insertion Sort"
    sort_name = "Heap Sort"

    list_size = 100
    list_size = 1_000
    list_size = 10_000

    # test_single_sorting_on_list_types(sort_name, list_size)
    test_sorting_algorithms_with_graphs(list_size, metric)
    # test_sorting_algorithms_with_prints(list_size)

if __name__ == '__main__':
    main()
