import random
import time


def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # Если символы совпадают
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Если не совпадают

    return dp[m][n]

time_diffs = []

for i in range(100):
    text1 = "".join([chr(random.randint(0, 128)) for _ in range(1000)])
    text2 = "".join([chr(random.randint(0, 128)) for _ in range(1000)])

    ts = time.time_ns()
    result = longest_common_subsequence(text1, text2)
    ts1 = time.time_ns()
    time_diff = ts1 - ts
    time_diffs.append(time_diff)

    print(f"i: {i}, result: {result}, execution time: {ts1}ns - {ts}ns = {time_diff}ns = {(time_diff)/1000}mcs = {(time_diff)/1000_000}ms = {(time_diff)/1000_000_000}s")

print(f"min:{min(time_diffs)/1_000_000}ms, max:{max(time_diffs)/1_000_000}ms, avg:{sum(time_diffs)/len(time_diffs)/1_000_000}ms" )