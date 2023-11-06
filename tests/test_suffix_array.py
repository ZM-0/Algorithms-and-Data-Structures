import unittest
from source.suffixes.suffix_array import *


# class TestCompareSuffixes(unittest.TestCase):
#     def test_banana_hl_1_1(self):
#         prefix_doubler: PrefixDoubler = PrefixDoubler("banana")
#         self.assertGreater(prefix_doubler.compare_suffixes(1, 3, 1), 0)
#
#     def test_banana_hl_1_2(self):
#         prefix_doubler: PrefixDoubler = PrefixDoubler("banana")
#         self.assertGreater(prefix_doubler.compare_suffixes(3, 5, 1), 0)


class TestBuildSuffixArray(unittest.TestCase):
    def test_banana(self):
        prefix_doubler: PrefixDoubler = PrefixDoubler("banana")
        self.assertEqual(prefix_doubler.build_suffix_array(), [6, 5, 3, 1, 0, 4, 2])


if __name__ == "__main__":
    unittest.main()
