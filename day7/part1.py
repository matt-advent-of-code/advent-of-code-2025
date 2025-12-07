def complete_manifold(diagram: str)  -> int:
    manifold = [list(line) for line in diagram.splitlines()]
    split_count = 0
    for i in range(1, len(manifold)):
        for j in range(0,len(manifold[i])):
            if manifold[i - 1][j] == 'S' or manifold[i - 1][j] == '|' and manifold[i][j] != '^':
                manifold[i][j] = '|'
            if (j + 1 < len(manifold[i])) and manifold[i][j + 1] == '^' and manifold[i - 1][j + 1] == '|':
                manifold[i][j] = "|"
                split_count += 1
            if manifold[i][j - 1] == '^' and manifold[i - 1][j - 1] == '|':
                manifold[i][j] = '|'
    return split_count


if __name__ == '__main__':
    with open('input.txt') as f:
        print(complete_manifold(f.read()))