import copy
import sys

import numpy as np
from typing import List, Tuple


def expand_zeros(field: np.ndarray, x: int, y: int) -> None:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= y + i < len(field) and 0 <= x + j < len(field[0]):
                field[y + i][x + j] = 0


def get_shortest_path_length(field: List[List[int]]) -> int:
    f = np.array(copy.deepcopy(field))
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 0:
                expand_zeros(f, x, y)
    min_length = sys.maxsize
    found = False
    for y in range(len(f)):
        if f[y][0] == f[y][1] == 1:
            exist, value = get_shortest(f[:, 1:], 0, y)
            if exist:
                min_length = min(min_length, value)
                found = True
    return min_length if found else -1


def get_shortest(field: np.ndarray, x: int, y: int) -> Tuple[bool, int]:
    visited = set()
    length = 2
    squares = [(x, y, length)]
    while squares:
        current = squares.pop(0)
        if current[0] == len(field[0]) - 1:
            return True, current[2]
        if current[:2] not in visited:
            visited.add(current[:2])
            neighbours = get_neighbours(field, *current)
            for neighbour in neighbours:
                if neighbour[:2] not in visited:
                    squares.append(neighbour)
    return False, -1


def get_neighbours(field: np.ndarray, x: int, y: int, length: int) -> List[Tuple[int, int, int]]:
    dx, dy = 1, 0
    neighbours = []
    nlength = length + 1
    for _ in range(4):
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(field) and 0 <= nx < len(field[0]) and field[ny][nx] == 1:
            neighbours.append((nx, ny, nlength))
        dx, dy = -dy, dx
    return neighbours


def main():
    with open('input.txt') as file:
        data = file.read()
        rows = data.split('\n')
        field = [[int(char) for char in row.split(' ')] for row in rows]

    print(get_shortest_path_length(field))


if __name__ == '__main__':
    main()
