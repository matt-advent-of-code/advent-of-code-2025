import math
class MathProblem:
    def __init__(self):
        self.numbers: [str]  = []
        self.operation : str
        self.problem_size: int = 0

    def solve(self) -> int:
        if self.operation == '*':
            return math.prod(self.to_cephalopod())
        return sum(self.to_cephalopod())

    def to_cephalopod(self) -> [int]:
        cephalopod_numbers: [int] = []
        max_length = max([len(number) for number in self.numbers])
        for i in range(0, max_length):
            cephalopod_str = ''
            for j in range(len(self.numbers)):
                cephalopod_str += self.numbers[j][i]
            cephalopod_numbers.append(int(cephalopod_str.strip()))

        return cephalopod_numbers

def parse(input: str) -> [MathProblem]:
    problems: [MathProblem] = []
    lines = input.splitlines()
    length=1
    operation=lines[-1][0]
    for i in range(1, len(lines[-1])):
        if lines[-1][i] != ' ':
            problem = MathProblem()
            problem.operation = operation
            problem.problem_size = length  - 1
            problems.append(problem)
            operation = lines[-1][i]
            length=1
        else:
            length += 1
    problem = MathProblem()
    problem.operation = operation
    problem.problem_size = length
    problems.append(problem)

    for i,line in enumerate(lines[:-1]):
        start=0
        for j in range(0, len(problems)):
            problem = problems[j]
            problem.numbers.append(line[start:start + problem.problem_size])
            start += problem.problem_size + 1
    return problems

def solve_homework(homework: str) -> int:
    math_problems = parse(homework)
    return sum([problem.solve() for problem in math_problems])

if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve_homework(f.read()))