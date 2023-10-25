# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Insertion Sort of Numbers
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def insertion_sort(numbers: list[int | float]) -> list[int | float]:
    """
    Sorts a list of numbers in non-decreasing order using insertion sort.
    Works by maintaining a sorted sublist and an unsorted sublist, and growing the sorted sublist
    by one item in each iteration. The sorted sublist is at the start of the list, and in each
    iteration the next unsorted element is shifted to its correct position in the sorted sublist.

    n - number of items in the list

                                Best case   Worst case  Average case
    Time complexity:            O(n^2)      O(n^2)      O(n^2)
    Auxiliary space complexity: O(1)        O(1)        O(1)

    :param numbers: A list of numbers.
    :return: The list of numbers sorted in non-decreasing order.
    """
    for i in range(1, len(numbers)):
        item: int | float = numbers[i]
        j: int = i - 1

        while j >= 0 and numbers[j] > item:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = item

    return numbers
