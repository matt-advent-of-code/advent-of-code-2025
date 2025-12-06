
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


def count_all_fresh_id(input: str) -> int:
    fresh_id_ranges = parse(input)[0]
    ranges = []
    for fresh_id_range in fresh_id_ranges:
        start, end = fresh_id_range.split('-')
        ranges.append([int(start), int(end)])

    combined_range = True
    while combined_range:
        combined_range = False
        for i in range(0, len(ranges)):
            for j in range(i + 1, len(ranges)):
                added = add_to_range(ranges[i], ranges[j][0], ranges[j][1])
                if added:
                    del ranges[j]
                    combined_range = True
                    break

    return sum(1 + end - start for start,end in ranges)

def add_to_range(current_range: [int, int], start: int, end: int) -> bool:
    current_range_start, current_range_end = current_range

    if start <= current_range_start and end >= current_range_end:
        current_range[0] = start
        current_range[1] = end
        return True
    if current_range_start <= start <= current_range_end:
        if current_range_end <= end:
            current_range[1] = end
            if current_range_start >= start:
                current_range[0] = start
            return True
        else:
            # new range is in this range
            return True
    if current_range_start <= end <= current_range_end:
        if start <= current_range_start:
            current_range[0] = start
            return True
        else:
            return True

    return False

if __name__ == '__main__':
    with open('input.txt') as f:
        print(count_all_fresh_id(f.read()))