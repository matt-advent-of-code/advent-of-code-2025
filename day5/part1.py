import re


def parse(input: str) -> ([str], [int]):
    fresh_ids = []
    available_ingredients = []
    line_count = 0
    lines = input.splitlines()
    for line in lines:
        line_count+=1
        if line == '':
            break
        fresh_ids.append(line)
    for i in lines[line_count:]:
        available_ingredients.append(int(i))
    return fresh_ids, available_ingredients

def is_fresh(fresh: [str], ingredient: int) -> bool:
    return any([int(r.split('-')[0]) <= ingredient <= int(r.split('-')[1]) for r in fresh])

def count_fresh(input: str) -> int:
    fresh_ids, available_ingredients = parse(input)
    return sum([is_fresh(fresh_ids, x) for x in available_ingredients])

if __name__ == '__main__':
    with open('input.txt') as f:
        print(count_fresh(f.read()))