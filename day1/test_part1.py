import unittest

from day1.part1 import Safe


class MyTestCase(unittest.TestCase):
    def test_crack(self):
        combination = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
        safe = Safe(start=50)
        password = safe.crack(combination)
        self.assertEqual(3, password)  # add assertion here


if __name__ == '__main__':
    unittest.main()
