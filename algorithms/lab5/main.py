import time

from rabin_karp import search


def test_best():
    start = time.perf_counter()
    res = search('abaacaadaabbaaabcaadabaaablablaaplecandlecrackle', 'aaba')
    print(f'Best in {(time.perf_counter() - start) * 1000} ms')
    print(res)


def test_avg():
    start = time.perf_counter()
    res = search('aabaacaadaabaabaaabaacaadabaaablablaaplecandlecrackleaabaaaba', 'aaba')
    print(f'Average in {(time.perf_counter() - start)*1000} ms')
    print(res)


def test_worst():
    start = time.perf_counter()
    res = search('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa')
    print(f'Worst in {(time.perf_counter() - start) * 1000} ms')
    print(res)


def main():
    # print(search('cbmcbmcbmcbmzn,n,nn,,', 'n'))
    test_best()
    test_avg()
    test_worst()


if __name__ == '__main__':
    main()
