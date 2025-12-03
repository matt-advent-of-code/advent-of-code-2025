import unittest

from day3.part1 import Bank, Escalator


class MyTestCase(unittest.TestCase):
    def test_bank(self):
        bank = Bank([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1])
        joltage = bank.largest_joltage()

        self.assertEqual(98, joltage)

    def test_bank2(self):
        bank = Bank([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9])
        joltage = bank.largest_joltage()

        self.assertEqual(89, joltage)

    def test_bank3(self):
        bank = Bank([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8])
        joltage = bank.largest_joltage()

        self.assertEqual(78, joltage)

    def test_bank4(self):
        bank = Bank([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1])
        joltage = bank.largest_joltage()

        self.assertEqual(92, joltage)

    def test_escalator(self):
        escaltor = Escalator("""987654321111111
811111111111119
234234234234278
818181911112111""")
        joltage = escaltor.joltage()

        self.assertEqual(357, joltage)


if __name__ == '__main__':
    unittest.main()
