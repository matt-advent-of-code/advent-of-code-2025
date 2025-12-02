import unittest

from day1.part1 import Safe
from day2.part1 import invalid_ids, sum_invalid


class MyTestCase(unittest.TestCase):
    def test_ids(self):
        invalid = invalid_ids("11-22")
        self.assertEqual([11, 22], invalid)

    def test_ids2(self):
        invalid = invalid_ids("95-115")
        self.assertEqual([99], invalid)

    def test_ids3(self):
        invalid = invalid_ids("998-1012")
        self.assertEqual([1010], invalid)

    def test_ids4(self):
        invalid = invalid_ids("1188511880-1188511890")
        self.assertEqual([1188511885], invalid)

    def test_ids5(self):
        invalid = invalid_ids("222220-222224")
        self.assertEqual([222222], invalid)

    def test_ids6(self):
        invalid = invalid_ids("1698522-1698528")
        self.assertEqual([], invalid)

    def test_ids7(self):
        invalid = invalid_ids("446443-446449")
        self.assertEqual([446446], invalid)

    def test_ids8(self):
        invalid = invalid_ids("38593856-38593862")
        self.assertEqual([38593859], invalid)
    def test_sum(self):
        sum_of_invalid = sum_invalid("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")
        self.assertEqual(1227775554, sum_of_invalid)

if __name__ == '__main__':
    unittest.main()