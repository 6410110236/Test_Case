import unittest
from Julius_Caesar import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_lowercase_letters(self):
        self.assertEqual(caesarCipher("abc", 1), "bcd")

    def test_uppercase_letters(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_mixed_case_letters(self):
        self.assertEqual(caesarCipher("AbC", 2), "CdE")

    def test_non_alphabetic_characters(self):
        self.assertEqual(caesarCipher("123!@#", 5), "123!@#")

    def test_large_shift_value(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")

    def test_negative_shift_value(self):
        self.assertEqual(caesarCipher("xyz", -3), "uvw")

if __name__ == '__main__':
    unittest.main()
