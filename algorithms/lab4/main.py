
def solve(w, h, corridor: str, tiles: dict, x: int, y: int, lookup={}) -> int:
    if x == w - 1: return 1 if y == 0 or y == h - 1 else 0
    if (x, y) not in lookup:
        result = 0
        result += solve(w, h, corridor, tiles, x + 1, y)
        for nx, ny in tiles[corridor[y*w + x]]:
            if nx > x: result += 0 if nx == x + 1 and ny == y else solve(w, h, corridor, tiles, nx, ny)
        lookup[x, y] = result
    return lookup[x, y]


def get_data(filename):
    tiles = {}
    with open(filename) as file:
        line = file.readline()
        w, h = [int(x) for x in line.split(sep=' ')]
        corridor = file.read().replace('\n', '')
        for i, letter in enumerate(corridor):
            x, y = i % w, i // w
            if letter not in tiles:
                tiles[letter] = []
            tiles[letter].append((x, y))
    return w, h, corridor, tiles


def main():
    w, h, corridor, tiles = get_data('ijones.in')
    result = 0
    for y in range(h):
        result += solve(w, h, corridor, tiles, 0, y)

    with open('ijones.out', 'w') as file_out:
        file_out.write(str(result))


if __name__ == '__main__':
    main()
