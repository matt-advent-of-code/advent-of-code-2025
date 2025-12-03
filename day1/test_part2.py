import unittest
from itertools import combinations

from day1.part2 import Safe


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
        self.assertEqual(6, password)  # add assert

    def test_right(self):
        combination = "R450"
        safe = Safe(start=50)
        password = safe.crack(combination)
        self.assertEqual(5, password)

    def test_right2(self):
        combination = "R500"
        safe = Safe(start=99)
        password = safe.crack(combination)
        self.assertEqual(5, password)

    def test_left(self):
        combination = "L450"
        safe = Safe(start=50)
        password = safe.crack(combination)
        self.assertEqual(5, password)

    def test_left2(self):
        combination = "L500"
        safe = Safe(start=99)
        password = safe.crack(combination)
        self.assertEqual(5, password)

    def test_left3(self):
        combination = "L99"
        safe = Safe(start=99)
        password = safe.crack(combination)
        self.assertEqual(1, password)

    def test_left4(self):
        combination = "L100"
        safe = Safe(start=99)
        password = safe.crack(combination)
        self.assertEqual(1, password)

    def test_left5(self):
        combination = "L199"
        safe = Safe(start=99)
        password = safe.crack(combination)
        self.assertEqual(2, password)

    def test_left5(self):
        combination = "L200"
        safe = Safe(start=99)
        password = safe.crack(combination)
        self.assertEqual(2, password)


    def test_crack1(self):
        combination = "L68"
        safe = Safe(start=50)
        password = safe.crack(combination)
        self.assertEqual(1, password)

    def test_crack2(self):
        combination = "L30"
        safe = Safe(start=82)
        password = safe.crack(combination)
        self.assertEqual(0, password)

    def test_crack3(self):
        combination = "R48"
        safe = Safe(start=52)
        password = safe.crack(combination)
        self.assertEqual(1, password)

    def test_crack4(self):
        combination = "L5"
        safe = Safe(start=0)
        password = safe.crack(combination)
        self.assertEqual(0, password)

    def test_crack5(self):
        combination = "R60"
        safe = Safe(start=95)
        password = safe.crack(combination)
        self.assertEqual(1, password)




if __name__ == '__main__':
    unittest.main()