import unittest
from ABAB import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):

    def test_no_deletions_needed(self):
        self.assertEqual(alternatingCharacters("ababab"), 0)

    def test_single_character_string(self):
        self.assertEqual(alternatingCharacters("a"), 0)

    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("abababab"), 0)

    def test_all_identical_characters(self):
        self.assertEqual(alternatingCharacters("aaaaa"), 4)

    def test_mixed_characters(self):
        self.assertEqual(alternatingCharacters("aabbaabb"), 4)

if __name__ == '__main__':
    unittest.main()
