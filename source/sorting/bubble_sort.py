# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Bubble Sort of Numbers
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def bubble_sort(numbers: list[int | float]) -> list[int | float]:
    """
    Sorts a list of numbers in non-decreasing order using bubble sort.
    Works by maintaining a sorted sublist and an unsorted sublist, and growing the sorted sublist
    by one item in each iteration. In each iteration, the largest unsorted item is shifted up to the
    start of the sorted sublist at the end of the list.

    n - number of items in the list

                                Best case   Worst case  Average case
    Time complexity:            O(n)        O(n^2)      O(n^2)
    Auxiliary space complexity: O(1)        O(1)        O(1)

    :param numbers: A list of numbers.
    :return: The list of numbers sorted in non-decreasing order.
    """
    for limit in range(len(numbers) - 1, 0, -1):
        swapped: bool = False

        # Don't swap beyond limit as numbers[limit + 1:] is the sorted sublist
        for i in range(limit):
            if numbers[i] > numbers[i + 1]:
                buffer: int | float = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = buffer
                swapped = True

        # Exit early if the list is already sorted
        if not swapped:
            break

    return numbers
