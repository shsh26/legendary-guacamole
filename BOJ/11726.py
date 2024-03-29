# -*- coding: utf-8 -*-
"""2xn 타일링

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

"""
import sys

sys.setrecursionlimit(10 ** 7)


dp = [-1] * 1001
dp[0] = 1
dp[1] = 1
dp[2] = 2


def f(n):
    if dp[n] == -1:
        dp[n] = (f(n - 1) + f(n - 2)) % 10007

    return dp[n]


print(f(int(input())))
