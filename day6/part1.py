import math

class MathProblem:
    def __init__(self):
        self.numbers: [int]  = []
        self.operation : str

    def solve(self) -> int:
        if self.operation == '*':
            return math.prod(self.numbers)
        return sum(self.numbers)

def parse(input: str) -> [MathProblem]:
    problems: [MathProblem] = []
    lines = input.splitlines()
    for i,line in enumerate(lines[:-1]):
        for j,number in enumerate(line.split()):
            if j >= len(problems):
                problem = MathProblem()
                problems.append(problem)
            problems[j].numbers.append(int(number))
    for i,operation in enumerate(lines[-1].split()):
        problems[i].operation = operation
    return problems

def solve_homework(homework: str) -> int:
    math_problems = parse(homework)
    return sum([problem.solve() for problem in math_problems])

if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve_homework(f.read()))