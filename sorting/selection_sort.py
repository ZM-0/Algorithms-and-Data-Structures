# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Selection Sort of Numbers
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def selection_sort(numbers: list[int | float]) -> list[int | float]:
    """
    Sorts a list of numbers in non-decreasing order using selection sort.
    Works by maintaining a sorted sublist and an unsorted sublist, and growing the sorted sublist
    by one item in each iteration.

    n - number of items in the list

                                Best case   Worst case  Average case
    Time complexity:            O(n^2)      O(n^2)      O(n^2)
    Auxiliary space complexity: O(1)        O(1)        O(1)

    :param numbers: A list of numbers.
    :return: The list of numbers sorted in non-decreasing order.
    """
    for i in range(len(numbers)):
        # Find minimum of numbers[i:]
        minimum_index: int = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minimum_index]:
                minimum_index = j

        # Swap minimum unsorted item to end of sorted sublist
        buffer: int | float = numbers[i]
        numbers[i] = numbers[minimum_index]
        numbers[minimum_index] = buffer

    return numbers
