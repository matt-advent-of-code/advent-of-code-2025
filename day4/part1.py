def parse(diagram: str) -> [[str]]:
    rolls = []
    for line in diagram.splitlines():
        rolls.append(list(line))
    return rolls

def is_accessible(rolls: [[str]], x: int, y: int) -> bool:
    if rolls[x][y] != '@':
        return False
    neighbor_count = 0
    if x + 1 < len(rolls):
        if rolls[x + 1][y] == '@':
            neighbor_count += 1
        if y + 1 < len(rolls[x + 1]) and rolls[x + 1][y + 1] == '@':
            neighbor_count += 1
        if y - 1 >= 0 and rolls[x + 1][y - 1] == '@':
            neighbor_count +=1
    if x - 1 >= 0:
        if rolls[x - 1][y] == '@':
            neighbor_count += 1
        if y + 1 < len(rolls[x - 1]) and rolls[x - 1][y + 1] == '@':
            neighbor_count += 1
        if y - 1 >= 0 and rolls[x - 1][y - 1] == '@':
            neighbor_count +=1

    if y + 1 < len(rolls[x]) and rolls[x][y + 1] == '@':
        neighbor_count += 1
    if y - 1 >= 0 and rolls[x][y - 1] == '@':
        neighbor_count += 1

    return neighbor_count < 4

def count_accessible(rolls: [[str]]) -> int:
    accessible = 0
    for x in range(0, len(rolls)):
        for y in range(0, len(rolls[x])):
            accessible += is_accessible(rolls, x, y)
    return accessible

if __name__ == '__main__':
    with open('input.txt') as f:
        rolls = parse(f.read())
        print(count_accessible(rolls))