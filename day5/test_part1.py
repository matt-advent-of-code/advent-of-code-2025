import unittest

from day5.part1 import parse, is_fresh, count_fresh


class MyTestCase(unittest.TestCase):
    def test_is_spoiled(self):
        parsed = parse("""3-5
10-14
16-20
12-18

1
5
8
11
17
32
""")
        self.assertFalse(is_fresh(parsed[0], 1))

    def test_is_fresh(self):
        parsed = parse("""3-5
10-14
16-20
12-18

1
5
8
11
17
32""")
        self.assertTrue(is_fresh(parsed[0], 5))

    def test_is_spoiled2(self):
        parsed = parse("""3-5
10-14
16-20
12-18

1
5
8
11
17
32""")
        self.assertFalse(is_fresh(parsed[0], 8))

    def test_count(self):
        fresh = count_fresh("""3-5
10-14
16-20
12-18

1
5
8
11
17
32
""")
        self.assertEqual(3, fresh)

if __name__ == '__main__':
    unittest.main()
