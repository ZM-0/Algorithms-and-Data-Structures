# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Quick Sort of Numbers
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class QuickSorter:
    """An implementation of quicksort using DNF partitioning and random pivot selection."""

    def __init__(self, numbers: list[int | float]) -> None:
        """
        Initializes the sorter with a list of numbers.
        :param numbers: A list of numbers.
        """
        self.numbers: list[int | float] = numbers

    def swap(self, first: int, second: int) -> None:
        """
        Swaps two items in the list.
        :param first: The index of the first item.
        :param second: The index of the second item.
        """
        buffer: int | float = self.numbers[first]
        self.numbers[first] = self.numbers[second]
        self.numbers[second] = buffer

    def dnf_partition(self, start: int, stop: int, pivot: int) -> tuple[int, int]:
        """
        Partitions a sublist of the numbers using DNF partitioning about the given pivot.
        Partitions numbers[start:stop] about the pivot.
        :param start: The inclusive start of the sublist to partition.
        :param stop: The exclusive stop of the sublist to partition.
        :param pivot: The pivot value.
        :return: The inclusive start of values == pivot, and the exclusive end of values == pivot.
        """
        low: int = start        # numbers[start:low] < pivot
        middle: int = start     # numbers[low:middle] == pivot
        high: int = stop        # numbers[high:stop] > pivot

        while middle < stop:
            if self.numbers[middle] < pivot:
                self.swap(low, middle)
                low += 1
                middle += 1
            elif self.numbers[middle] == pivot:
                middle += 1
            else:
                self.swap(middle, high - 1)
                high -= 1

        return low, middle

    def sort(self, start: int = 0, stop: int | None = None) -> list[int | float]:
        """
        Sorts the numbers in non-decreasing order using quicksort.
        :param start: The inclusive start of the sublist to sort.
        :param stop: The exclusive stop of the sublist to sort.
        :return: The sorted list.
        """
        stop = len(self.numbers) if stop is None else stop

        if stop - start < 2:
            return self.numbers

        pivot: int = self.numbers[(start + stop) // 2]
        left, right = self.dnf_partition(start, stop, pivot)
        self.sort(start, left)
        self.sort(right, stop)
        return self.numbers
