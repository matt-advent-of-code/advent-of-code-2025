class Dial:
    def __init__(self, start: int, max: int):
        self.position = start
        self.max = max

    def rotate_right(self, distance: int):
        self.position = (self.position + distance) % (self.max + 1)

    def rotate_left(self, distance: int):
        self.position = (self.position - distance + (self.max + 1)) % (self.max + 1)

class Instruction:
    def __init__(self, direction: str, distance: int):
        self.direction = direction
        self.distance = distance


class Safe:
    max : int = 99
    def __init__(self, start: int):
        self.dial = Dial(start, 99)

    def crack(self, combination: str) -> int:
        password : int = 0
        instructions = parse(combination)
        for instruction in instructions:
            if instruction.direction == 'R':
                self.dial.rotate_right(instruction.distance)
            else:
                self.dial.rotate_left(instruction.distance)
            print(self.dial.position)
            if self.dial.position == 0:
                password += 1
        return password

def parse(combination: str) -> [Instruction]:
    return [Instruction(direction=(x[0]), distance=int(x[1:])) for x in combination.splitlines()]


if __name__ == '__main__':
    safe = Safe(50)
    with open('input.txt') as f:
        print(safe.crack(f.read()))