# -*- coding: utf-8 -*-
"""알약
"""

dp = [[0] * 32 for _ in range(32)]

for w in range(1, 31):
    for h in range(31):
        if h > w:
            continue
        if h == 0:
            dp[w][h] = 1
        else:
            dp[w][h] = dp[w - 1][h] + dp[w][h - 1]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])
