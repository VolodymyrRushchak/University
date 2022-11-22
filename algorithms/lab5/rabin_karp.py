from typing import List

alphabet = 256
p = 12456131


def my_hash(txt: str) -> int:
    result = 0
    n = len(txt)
    for i, ch in enumerate(txt):
        result += ord(ch) * alphabet ** (n - i - 1)
    return result % p


def update_hash(old_hash: int, old_first: str, last: str, m) -> int:
    new_hash = (old_hash - ord(old_first) * alphabet ** (m - 1)) * alphabet + ord(last)
    return new_hash % p


def search(txt: str, pat: str) -> List[int]:
    txt_len = len(txt)
    txt = txt + 'x'
    occurrences = []
    pat_len = len(pat)
    pat_hash = my_hash(pat)
    substr_hash = my_hash(txt[:pat_len])
    for start in range(txt_len - pat_len + 1):
        if pat_hash == substr_hash and txt[start:start+pat_len] == pat:
            occurrences.append(start)
        substr_hash = update_hash(substr_hash, txt[start], txt[start+pat_len], pat_len)
    return occurrences
