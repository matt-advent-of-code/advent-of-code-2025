import unittest

from day5.part2 import count_all_fresh_id


class MyTestCase(unittest.TestCase):
    def test_count_fresh(self):
        input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
        self.assertEqual(14, count_all_fresh_id(input))
    def test_count_fresh2(self):
        input = """3-5
10-14
16-20
12-18
2-4

1
5
8
11
17
32
"""
        self.assertEqual(15, count_all_fresh_id(input))

    def test_count_fresh3(self):
        input = """3-5
2-8

1
5
8
11
17
32
"""
        self.assertEqual(7, count_all_fresh_id(input))

    def test_count_fresh4(self):
        input = """2-8
3-5

1
5
8
11
17
32
"""
        self.assertEqual(7, count_all_fresh_id(input))

    def test_count_fresh5(self):
        input = """2-8
8-9

1
5
8
11
17
32
"""
        self.assertEqual(8, count_all_fresh_id(input))


if __name__ == '__main__':
    unittest.main()
