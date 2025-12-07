import unittest

from day6.part1 import MathProblem, solve_homework


class MyTestCase(unittest.TestCase):
    def test_solve1(self):
        problem = MathProblem()
        problem.numbers = [123, 45, 6]
        problem.operation = '*'

        self.assertEqual(33210, problem.solve())

    def test_solve2(self):
        problem = MathProblem()
        problem.numbers = [328, 64, 98]
        problem.operation = '+'

        self.assertEqual(490, problem.solve())

    def test_homework(self):
        homework = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """
        answer = solve_homework(homework)

        self.assertEqual(4277556, answer)



if __name__ == '__main__':
    unittest.main()
