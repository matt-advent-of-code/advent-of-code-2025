import unittest

from day4.part1 import parse, is_accessible, count_accessible


class MyTestCase(unittest.TestCase):
    def test_parse(self):
        rolls = parse(""".@
@.
""")
        expected = [['.', '@'],
                    ['@', '.']]
        self.assertEqual(expected, rolls)  # add assertion here

    def test_not_roll(self):
        rolls = [['.', '@'],
                ['@', '.']]
        self.assertFalse(is_accessible(rolls, 0, 0))

    def test_top_right(self):
        rolls = [['.', '@'],
                ['@', '.']]
        self.assertTrue(is_accessible(rolls, 0, 1))

    def test_bottom_let(self):
        rolls = [['.', '@'],
                ['@', '.']]
        self.assertTrue(is_accessible(rolls, 1, 0))


    def test_middle(self):
        rolls = [['.', '@', '.'],
                 ['@', '@', '.'],
                 ['@', '.', '.']]
        self.assertTrue(is_accessible(rolls, 1, 1))

    def test_not_accessible(self):
        rolls = [['.', '@', '.'],
                 ['@', '@', '.'],
                 ['@', '@', '.']]
        self.assertFalse(is_accessible(rolls, 1, 1))

    def test_puzzle(self):
        puzzle_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
        rolls = parse(puzzle_input)
        self.assertEqual(13, count_accessible(rolls))


if __name__ == '__main__':
    unittest.main()
