from typing import List, Tuple


def get_input() -> List[Tuple[int, int]]:
    row_num = int(input())
    input_rows = []
    for _ in range(row_num):
        row = [int(num) for num in input().split(' ')]
        input_rows.append((row[0], row[1]))
    return input_rows


def get_comb_num(input_list: List[Tuple[int, int]]) -> int:
    tribe_of = {}
    tribe_count = 0
    tribes = [[0, 0]]
    for a, b in input_list:
        is_a, is_b = a in tribe_of.keys(), b in tribe_of.keys()
        if not is_a and not is_b:
            tribe_of[a] = tribe_count
            tribe_of[b] = tribe_count
            tribes[tribe_count][a % 2] += 1
            tribes[tribe_count][b % 2] += 1
            tribe_count += 1
            tribes.append([0, 0])
        elif not is_a:
            tribe_of[a] = tribe_of[b]
            tribes[tribe_of[b]][a % 2] += 1
        elif not is_b:
            tribe_of[b] = tribe_of[a]
            tribes[tribe_of[a]][b % 2] += 1
    total_girls = sum((tribe[0] for tribe in tribes))
    result = 0
    for girls, boys in tribes:
        result += boys * (total_girls - girls)
    return result


def main():
    input_rows = get_input()
    result = get_comb_num(input_rows)
    print(result)


if __name__ == '__main__':
    main()
