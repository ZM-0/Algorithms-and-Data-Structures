# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Boyer-Moore Exact Pattern Matching
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from z_algorithm import build_z_array


class BoyerMooreMatcher:
    """An implementation of the Boyer-Moore algorithm for exact pattern matching."""

    def __init__(self, text: str, pattern: str):
        """
        Initializes the matcher with a text and pattern string.
        :param text: A text string.
        :param pattern: A pattern string.
        :raises ValueError: Raised if the pattern is longer than the text.
        """
        if len(text) < len(pattern):
            raise ValueError("The pattern cannot be longer than the text")

        self.text: str = text
        self.pattern: str = pattern
        self.text_index: int = len(pattern) - 1
        self.pattern_index: int = len(pattern) - 1

        self.extended_bad_characters: list[dict[str, int]] = [dict() for _ in range(len(pattern))]
        """extended_bad_character_positions[i][c] is the index of the rightmost occurrence of
        character c in pattern[:i + 1]. If there is no such occurrence of character c, there is no
        key for c in the dictionary extended_bad_character_positions[i]."""
        self.build_extended_bad_character_positions()

        self.good_suffixes: list[int] = self.build_good_suffixes()
        """good_suffix[i] is the inclusive endpoint of the rightmost occurrence of pattern[i:] in
        the pattern that is not a suffix, or -1 if no such occurrence exists."""

        self.borders: list[int] = self.build_borders()
        """borders[i] is the length of the longest suffix of pattern[i:] that matches a prefix of
        the pattern."""

    def build_extended_bad_character_positions(self) -> None:
        """
        Finds the rightmost occurrences of each character for each prefix of the pattern.
        This is a list of dictionaries where positions[i][c] is the index of the rightmost occurrence
        of character c in pattern[0:i + 1]. If character c doesn't occur in pattern[0:i + 1], there
        will be no such key c in the relevant dictionary.
        """
        for i in range(len(self.pattern)):
            for j in range(i + 1):
                self.extended_bad_characters[i][self.pattern[j]] = j

    def build_good_suffixes(self) -> list[int]:
        """
        Finds the inclusive endpoints of the rightmost occurrences of each suffix of the pattern,
        or -1 if no such occurrence exists.
        """
        # Find an array z_suffix where z_suffix[i] is the length of the longest substring of the
        # pattern ending at index i inclusive that matches a suffix of the pattern
        reversed_pattern: str = ''.join(reversed(self.pattern))
        z_suffix: list[int] = build_z_array(reversed_pattern)
        z_suffix.reverse()

        good_suffixes: list[int] = [-1 for _ in range(len(self.pattern))]

        for i in range(len(self.pattern)):
            j: int = len(self.pattern) - z_suffix[i]    # The inclusive start of the matched suffix
            self.good_suffixes[j] = i

        return good_suffixes

    def build_borders(self) -> list[int]:
        """
        Finds the length of the longest suffix of each suffix of the pattern that matches a prefix
        of the pattern.
        """
        pattern_z_array: list[int] = build_z_array(self.pattern)
        longest_border: int = 0     # The length of the longest border seen so far

        borders: list[int] = [0 for _ in range(len(self.pattern))]

        # Find the borders right-to-left
        for i in reversed(range(len(self.pattern))):
            border: int = pattern_z_array[i]

            # A new border is found if the z-box ends at the pattern end
            if i + border == len(self.pattern):
                longest_border = max(longest_border, border)

            borders[i] = longest_border

        return borders

    def get_extended_bad_character_jump(self) -> int:
        """
        :return: The jump length based on the extended bad character rule.
        """
        if self.pattern_index == 0:
            return 1

        bad_character: str = self.text[self.text_index]
        position: int = self.extended_bad_characters[self.pattern_index - 1].get(bad_character, -1)
        return self.pattern_index - position

    def get_good_suffix_jump(self) -> int:
        """
        :return: The jump length based on the good suffix rule.
        """
        return len(self.pattern) - self.good_suffixes[self.pattern_index + 1] - 1

    def get_matched_prefix_jump(self) -> int:
        """
        :return: The jump length based on the matched prefix rule.
        """
        return len(self.pattern) - self.borders[self.pattern_index + 1]

    def match(self) -> list[int]:
        """
        Finds exact occurrences of the pattern in the text.
        :return: A list of the inclusive start-points of the matches in the text.
        """
        matches: list[int] = []

        while self.text_index + len(self.pattern) - self.pattern_index <= len(self.text):
            # Scan the pattern with the text right to left
            while (self.text_index >= 0 and self.pattern_index >= 0 and
                   self.text[self.text_index] == self.pattern[self.pattern_index]):
                self.text_index -= 1
                self.pattern_index -= 1

            if self.pattern_index == -1:
                # Detect match
                matches.append(self.text_index + 1)
            else:
                # Jump the pattern along the text
                jump1: int = self.get_extended_bad_character_jump()
                jump2: int = self.get_good_suffix_jump()
                jump3: int = self.get_matched_prefix_jump()
                jump: int

                if jump2 > 0:
                    jump = max(jump1, jump2)
                else:
                    jump = max(jump1, jump3)

                self.text_index += len(self.pattern) - self.pattern_index + jump - 1
                self.pattern_index = len(self.pattern) - 1

        return matches
