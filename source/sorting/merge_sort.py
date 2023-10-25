# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Merge Sort of Numbers
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class MergeSorter:
    """Implements merge sorting of numbers."""

    def __init__(self, numbers: list[int | float]):
        """
        Initializes a merge sorter.
        :param numbers: A list of numbers.
        """
        self.numbers: list[int | float] = numbers

    def merge(self, left_start: int, left_stop: int, right_start: int, right_stop: int) -> list[int | float]:
        """
        Merges two sorted sub-lists into one list.
        :param left_start: The inclusive start of the left sorted sublist.
        :param left_stop: The exclusive stop of the left sorted sublist.
        :param right_start: The inclusive start of the right sorted sublist.
        :param right_stop: The exclusive stop of the right sorted sublist.
        :return: The combined sorted list.
        """
        merged: list[int | float] = []
        i: int = left_start
        j: int = right_start

        while i < left_stop or j < right_stop:
            if j >= right_stop or i < left_stop and self.numbers[i] <= self.numbers[j]:
                merged.append(self.numbers[i])
                i += 1
            else:
                merged.append(self.numbers[j])
                j += 1

        return merged

    def sort(self, start: int = 0, stop: int | None = None) -> list[int | float]:
        """
        Sorts a list of numbers in non-decreasing order using merge sort.
        Works by recursively sorting the two halves of the input list, and merging the two sorted halves.

        n - number of items in the list

                                    Best case       Worst case      Average case
        Time complexity:            O(n * log(n))   O(n * log(n))   O(n * log(n))
        Auxiliary space complexity: O(n)            O(n)            O(n)

        :param start: The inclusive start of the sublist to be sorted.
        :param stop: The exclusive stop of the sublist to be sorted.
        :return: The list of numbers sorted in non-decreasing order.
        """
        stop = len(self.numbers) if stop is None else stop

        if stop - start < 2:
            return self.numbers  # Single element doesn't need sorting

        middle: int = (start + stop) // 2   # Get middle or upper middle
        self.sort(start, middle)
        self.sort(middle, stop)
        self.numbers[start:stop] = self.merge(start, middle, middle, stop)
        return self.numbers
