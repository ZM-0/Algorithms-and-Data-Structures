# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Suffix Array Construction Using Prefix-Doubling
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class PrefixDoubler:
    """Builds a suffix array using prefix-doubling."""

    def __init__(self, string: str) -> None:
        """
        Initializes a prefix-doubling suffix array builder.
        :param string: The string to build the suffix array of.
        """
        self.string: str = string
        self.suffix_array: list[int] = [i for i in range(len(string))]
        self.rank: list[int] = [ord(c) for c in string]    # This already sorts by the first character

    def swap(self, first: int, second: int) -> None:
        """
        Swaps two items in the suffix array.
        :param first: The index of the first item.
        :param second: The index of the second item.
        """
        buffer: int | float = self.suffix_array[first]
        self.suffix_array[first] = self.suffix_array[second]
        self.suffix_array[second] = buffer

    def compare_suffixes(self, suffix1: int, suffix2: int, half_length: int) -> int:
        """
        Compares two suffixes by their first few characters.
        :param suffix1: The inclusive start of the first suffix.
        :param suffix2: The inclusive start of the second suffix.
        :param half_length: Half the number of characters to compare by.
        :return: An integer > 0 if suffix1 > suffix2, 0 if suffix == suffix2, < 0 if suffix1 < suffix2.
        """
        if self.rank[suffix1] != self.rank[suffix2]:
            # Compare by first halves
            return self.rank[suffix1] - self.rank[suffix2]
        elif suffix1 + half_length < len(self.string) and suffix2 + half_length < len(self.string):
            # Compare by second halves
            return self.rank[suffix1 + half_length] - self.rank[suffix2 + half_length]
        else:
            # Compare by length
            return suffix2 - suffix1

    def dnf_partition(self, start: int, stop: int, pivot: int, half_length: int) -> tuple[int, int]:
        """
        Partitions a sublist of the suffix array using DNF partitioning about the given pivot.
        Partitions numbers[start:stop] about the pivot.
        :param start: The inclusive start of the sublist to partition.
        :param stop: The exclusive stop of the sublist to partition.
        :param pivot: The pivot value.
        :param half_length: Half the number of characters to compare the suffixes by.
        :return: The inclusive start of values == pivot, and the exclusive end of values == pivot.
        """
        low: int = start        # suffix_array[start:low] < pivot
        middle: int = start     # suffix_array[low:middle] == pivot
        high: int = stop        # suffix_array[high:stop] > pivot

        while middle < stop:
            if self.compare_suffixes(self.suffix_array[middle], pivot, half_length) < 0:
                self.swap(low, middle)
                low += 1
                middle += 1
            elif self.compare_suffixes(self.suffix_array[middle], pivot, half_length) == 0:
                middle += 1
            else:
                self.swap(middle, high - 1)
                high -= 1

        return low, middle

    def sort(self, half_length: int, start: int = 0, stop: int | None = None) -> None:
        """
        Sorts the suffixes in the suffix array based on the first k characters.
        :param half_length: Half the number of characters to compare each suffix by.
        :param start: The inclusive start of the sublist to sort.
        :param stop: The exclusive stop of the sublist to sort.
        """
        stop = len(self.suffix_array) if stop is None else stop

        if stop - start > 1:
            pivot: int = self.suffix_array[(start + stop) // 2]
            left, right = self.dnf_partition(start, stop, pivot, half_length)
            self.sort(half_length, start, left)
            self.sort(half_length, right, stop)

    def update_rank(self, half_length: int) -> None:
        """
        Updates the ranks of all the suffixes.
        :param half_length: Half the number of characters the suffixes have been sorted by.
        """
        new_rank: list[int] = [0 for _ in range(len(self.string))]

        for i in range(len(self.suffix_array) - 1):
            suffix: int = self.suffix_array[i]
            next_suffix: int = self.suffix_array[i + 1]
            step: int = 1 if self.compare_suffixes(next_suffix, suffix, half_length) > 0 else 0
            new_rank[next_suffix] = new_rank[suffix] + step

        self.rank = new_rank

    def build_suffix_array(self) -> list[int]:
        """
        Builds the suffix array of the string using prefix-doubling.
        :return: A list of the inclusive start-points of all the suffixes of the string, sorted
        by the suffixes.
        """
        # For each comparison length from 1 to n characters, doubling:
        half_length: int = 1
        while half_length <= len(self.string):
            # Sort the suffixes by their first few characters
            self.sort(half_length)

            # Update the rank array
            self.update_rank(half_length)

            half_length *= 2

        return self.suffix_array
