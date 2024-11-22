from __future__ import annotations
from typing import List

class Change:
    def __init__(self, text: str, change_type: str) -> None:
        self.text = text
        self.change_type = change_type

    def __repr__(self) -> str:
        return f"{self.change_type} {self.text}"

def compute_lcs(text1: List[str], text2: List[str]) -> List[List[int]]:
    n, m = len(text1), len(text2)

    lcs = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs

def diff(text1: List[str], text2: List[str]) -> List[Change]:
    lcs = compute_lcs(text1, text2)
    results = []

    i, j = len(text1), len(text2)

    while i > 0 or j > 0:
        if i == 0:
            results.append(Change(text2[j - 1][:-1], "+"))
            j -= 1
        elif j == 0:
            results.append(Change(text1[i - 1][:-1], "-"))
            i -= 1
        elif text1[i - 1] == text2[j - 1]:
            results.append(Change(text1[i - 1][:-1], " "))
            i -= 1
            j -= 1
        elif lcs[i - 1][j] >= lcs[i][j - 1]:
            results.append(Change(text1[i - 1][:-1], "-"))
            i -= 1
        else:
            results.append(Change(text2[j - 1][:-1], "+"))
            j -= 1

    return list(reversed(results))

def read_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

def main(file1: str, file2: str) -> None:
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    changes = diff(lines1, lines2)

    [print(change) for change in changes if str(change)[1:].strip()]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: main.py <file1> <file2>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
