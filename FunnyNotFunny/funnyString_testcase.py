import unittest
from funnyString import funnyString

class TestFunnyString(unittest.TestCase):

    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_not_funny_string(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_funny_string_with_repeated_characters(self):
        self.assertEqual(funnyString("aaaa"), "Funny")

    def test_funny_string_single_character(self):
        self.assertEqual(funnyString("a"), "Funny")  # Updated assertion

    def test_funny_string_empty(self):
        self.assertEqual(funnyString(""), "Funny")

if __name__ == '__main__':
    unittest.main()
