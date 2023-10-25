# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exact Pattern Matching Using The Z-array
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from z_algorithm import build_z_array


def z_match(text: str, pattern: str) -> list[int]:
    """
    Finds exact matches of the pattern in the text using the z-array of the combined pattern and
    text.
    Works by building the z-array for the combined pattern and text, and then using that to find
    substring matches of the pattern in the text.

    n - number of characters in the text
    m - number of characters in the pattern
    c - number of matches

    Time complexity:            O(n + m)
    Auxiliary space complexity: O(n + m + c)

    :param text: A text string.
    :param pattern: A pattern string.
    :return: A list of the inclusive start-points of the matches of the pattern in the text.
    :raises ValueError: Raised if the pattern is longer than the text.
    """
    if len(text) < len(pattern):
        raise ValueError("The pattern cannot be longer than the text")

    combined_string: str = pattern + '$' + text     # Assume '$' doesn't occur in the pattern or text
    z_array: list[int] = build_z_array(combined_string)
    matches: list[int] = []

    for i in range(len(text)):
        if z_array[len(pattern) + 1 + i] == len(pattern):
            matches.append(i)

    return matches
