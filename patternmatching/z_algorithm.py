# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Gusfield's Z-array and Z-array Construction Algorithm
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from typing import Optional


def match(string: str, i: int, j: int) -> int:
    """
    Manually matches two substrings of a string.
    :param string: A character string.
    :param i: The inclusive startpoint of the first substring.
    :param j: The inclusive startpoint of the second substring.
    :return: The length of the match.
    """
    length: int = 0

    while (i + length < len(string) and j + length < len(string) and
           string[i + length] == string[j + length]):
        length += 1

    return length


def build_z_array(string: str) -> list[int]:
    """
    Builds the z-array of a string using Gusfield's linear time construction algorithm.
    :param string: A character string.
    :return: The z-array of the string. The value at index i is the length of the longest substring
    starting at index i inclusive that matches a prefix of the string.
    """
    # The first z-value is trivially the length of the string
    z_array: list[int] = [len(string) for _ in range(len(string))]

    left: Optional[int] = None      # The inclusive startpoint of the z-box ending at right
    right: Optional[int] = None     # The exclusive endpoint of the rightmost z-box seen so far

    for i in range(1, len(string)):
        if right is None or i >= right:
            length: int = match(string, 0, i)
            z_array[i] = length

            if length > 0:
                left = i
                right = i + length
        elif z_array[i - left] < right - i:
            z_array[i] = z_array[i - left]
        elif z_array[i - left] == right - i:
            extension: int = match(string, right - i, right)
            z_array[i] = right - i + extension

            if extension > 0:
                left = i
                right = i + z_array[i]
        else:
            z_array[i] = right - i

    return z_array
