import random
import time
import timeit


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


text1 = "".join([chr(random.randint(0, 10000)) for _ in range(10000)])
print(text1)
text2 = "ace"

ts = time.time_ns()
result = longest_common_subsequence(text1, text2)
ts1 = time.time_ns()

print(f"result: {result}, execution time:{ts1}-{ts}={ts1-ts}")