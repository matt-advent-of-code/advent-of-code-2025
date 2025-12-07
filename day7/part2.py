def complete_manifold(diagram: str)  -> [[str]]:
    manifold = [list(line) for line in diagram.splitlines()]
    for i in range(1, len(manifold)):
        for j in range(0,len(manifold[i])):
            if manifold[i - 1][j] == 'S' or manifold[i - 1][j] == '|' and manifold[i][j] != '^':
                manifold[i][j] = '|'
            if (j + 1 < len(manifold[i])) and manifold[i][j + 1] == '^' and manifold[i - 1][j + 1] == '|':
                manifold[i][j] = "|"
            if manifold[i][j - 1] == '^' and manifold[i - 1][j - 1] == '|':
                manifold[i][j] = '|'
    return manifold


def count_splits(timeline_counts: dict[(int,int), int], manifold: [[str]], i: int, j: int) -> int:
    while manifold[i][j] != '^' and i < len(manifold) - 1:
        i+=1
    if manifold[i][j] == '^':
        return timeline_counts[(i,j)]
    return 1

def count_timelines(diagram: str) -> int:
    timeline_counts: dict[(int,int), int] = {}
    manifold = complete_manifold(diagram)
    timeline_count = 0
    for i in range(len(manifold) - 2, 0, -1):
        for j in range(0, len(manifold[i])):
            if manifold[i][j] == '^':
                left = count_splits(timeline_counts, manifold, i + 1, j - 1)
                right = count_splits(timeline_counts, manifold, i + 1, j + 1)
                timeline_counts[(i, j)] = left + right
                timeline_count = left + right

    return timeline_count

def split(manifold: [[str]], i: int, j: int) -> int:

    for i in range(i, len(manifold)):
        for j in range(j, len(manifold)):
            if  manifold[i - 1][j] == '|' and manifold[i][j] != '^':
                manifold[i][j] = '|'






if __name__ == '__main__':
    with open('input.txt') as f:
        print(count_timelines(f.read()))










