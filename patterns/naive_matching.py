# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Naive Exact Pattern Matching
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def naive_match(text: str, pattern: str) -> list[int]:
    """
    Naively finds the occurrences in the text where the pattern matches exactly.
    Works by manually comparing the pattern at every alignment with the text.

    n - number of characters in the text
    m - number of characters in the pattern
    c - number of matches

                                Worst case  Best case
    Time complexity:            O(n * m)    O(n)
    Auxiliary space complexity: O(c)        O(c)

    :param text: A text string.
    :param pattern: A pattern string.
    :return: A list of the inclusive starting positions in the text where the pattern matches.
    :raises ValueError: Raised when the pattern is longer than the text.
    """
    if len(text) < len(pattern):
        raise ValueError("The pattern cannot be longer than the text")

    matches: list[int] = []

    for i in range(len(text) - len(pattern)):
        j: int = 0

        while j < len(pattern) and text[i + j] == pattern[j]:
            j += 1

        if j == len(pattern):
            matches.append(i)

    return matches
