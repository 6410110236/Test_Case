import unittest
from swap import alternate

class TestAlternate(unittest.TestCase):

    def test_alternate_string(self):
        self.assertEqual(alternate("abaacd"), 2)

    def test_single_character_string(self):
        self.assertEqual(alternate("a"), 1)

    def test_all_identical_characters(self):
        self.assertEqual(alternate("aaaa"), 1)

    def test_mixed_characters(self):
        self.assertEqual(alternate("abcabc"), 4)

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)

    def test_repeated_pairs(self):
        self.assertEqual(alternate("ababab"), 6)

if __name__ == '__main__':
    unittest.main()
