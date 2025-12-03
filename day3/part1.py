class Bank:
    def __init__(self, batteries: [int]):
        self.batteries = batteries

    def largest_joltage(self) -> int:
        first = max(self.batteries[:-1])
        index_of_largest = self.batteries.index(first)
        second = max(self.batteries[index_of_largest + 1:])
        return int(str(first) + str(second))

class Escalator:
    def __init__(self, banks: str):
        self.banks = []
        for line in banks.splitlines():
            bank = Bank([int(battery) for battery in [x for x in line]])
            self.banks.append(bank)

    def joltage(self):
        return sum([bank.largest_joltage() for bank in self.banks])
if __name__ == '__main__':
    with open('input.txt') as f:
        escalator = Escalator(f.read())
        print(escalator.joltage())