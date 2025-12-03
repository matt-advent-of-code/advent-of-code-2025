class Bank:
    def __init__(self, batteries: [int]):
        self.batteries = batteries

    def largest_joltage(self) -> int:
        start_index = 0
        end_index = -11
        batteries = []
        for i in range(0, 12):
            battery, index = self.find_largest(start_index, end_index)
            batteries.append(str(battery))
            end_index+=1
            start_index = index + 1

        return int(''.join(batteries))


    def find_largest(self, start_index, end_index) -> tuple[int, int]:
        if end_index == 0:
            largest = max(self.batteries[start_index:])
            index = self.batteries[start_index:].index(largest) + start_index
        else:
            largest = max(self.batteries[start_index:end_index])
            index = self.batteries[start_index:end_index].index(largest) + start_index
        return largest, index


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