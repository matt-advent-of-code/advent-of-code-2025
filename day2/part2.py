import numpy as np

def invalid_ids(id_range: str) -> [int]:
    start = int(id_range.split("-")[0])
    end = int(id_range.split("-")[1])
    ids = [x for x in range(start, end + 1)]
    return list(filter(is_invalid, ids))

def is_invalid(candidate: str) -> bool:
    for i in range(1, len(str(candidate))):
        l = np.array_split(list(str(candidate)), i + 1)
        invalid = True
        for x in l:
            if str(x) != str(l[0]):
                invalid = False
        if invalid:
            return invalid
    return False

def sum_invalid(id_ranges : str) -> int:
    id_sum = 0
    for id_range in id_ranges.split(","):
        invalid = invalid_ids(id_range)
        id_sum += sum(invalid)
    return id_sum

if __name__ == '__main__':
    with open('input.txt') as f:
        print(sum_invalid(f.read()))