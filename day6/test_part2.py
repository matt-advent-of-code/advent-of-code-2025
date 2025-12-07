import unittest

from day6.part2 import MathProblem, solve_homework


class MyTestCase(unittest.TestCase):

    def test_solve1(self):
        problem = MathProblem()
        problem.numbers = ['64 ','23 ', '314']
        problem.operation = '+'

        self.assertEqual(1058, problem.solve())

    def test_solve2(self):
        problem = MathProblem()
        problem.numbers = [' 51', '387', '215']
        problem.operation = '*'

        self.assertEqual(3253600, problem.solve())

    def test_solve3(self):
        problem = MathProblem()
        problem.numbers = ['328', '64 ', '98 ']
        problem.operation = '+'

        self.assertEqual(625, problem.solve())

    def test_solve4(self):
        problem = MathProblem()
        problem.numbers = ['123', ' 45', '  6']
        problem.operation = '*'

        self.assertEqual(8544, problem.solve())

    def test_homework(self):
        homework = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
        answer = solve_homework(homework)

        self.assertEqual(3263827, answer)


    def test_solve5(self):
        problem = MathProblem()
        problem.numbers = ['2477',
                           '3524',
                           '6243',
                           '  44']
        problem.operation = '+'
        # 7434 + 7244 + 452 + 236
        self.assertEqual(15366, problem.solve())

    def test_solve6(self):
        problem = MathProblem()
        problem.numbers = ['92',
                           ' 4',
                           ' 4',
                           ' 4']
        problem.operation = '*'
        # 2444 * 9
        self.assertEqual(21996, problem.solve())

    def test_solve7(self):
        problem = MathProblem()
        problem.numbers = ['399',
                           '525',
                           '595',
                           '677']
        problem.operation = '*'
        # 9557 * 9297 * 3556
        self.assertEqual(315955681524, problem.solve())

    def test_solve8(self):
        problem = MathProblem()
        problem.numbers = ['956',
                           '936',
                           '999',
                           '  9']
        problem.operation = '*'
        # 999 * 539 * 6699
        self.assertEqual(3607150239, problem.solve())


    def test_homework_2(self):
        homework = """2477 92 399 956 
3524  4 525 936
6243  4 595 999
  44  4 677   9
+    *  *   *  """

        answer = solve_homework(homework)
        self.assertEqual(319562869125, answer)



if __name__ == '__main__':
    unittest.main()
