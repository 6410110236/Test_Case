import unittest
from rearrange import gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_non_decreasing_order(self):
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")

    def test_non_decreasing_order_mixed(self):
        self.assertEqual(gridChallenge(["cba", "fed", "igh"]), "YES")

    def test_not_non_decreasing_order(self):
        self.assertEqual(gridChallenge(["abc", "edf", "ghi"]), "YES")

    def test_empty_grid(self):
        self.assertEqual(gridChallenge([]), "YES")

    def test_single_row(self):
        self.assertEqual(gridChallenge(["cba"]), "YES")

    def test_single_column(self):
        self.assertEqual(gridChallenge(["c", "b", "a"]), "NO")

if __name__ == '__main__':
    unittest.main()
