# -*- coding: utf-8 -*-
"""이항 계수 2

자연수 N과 정수 K가 주어졌을 때
이항 계수 bino(N,K)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)

bino(N, K)를 10,007로 나눈 나머지를 출력한다.
"""
import sys

sys.setrecursionlimit(10 ** 7)

dp = [[-1] * 1001 for _ in range(1001)]


def f(n, k):
    if dp[n][k] == -1:
        if k == 0 or n == k:
            dp[n][k] = 1
        else:
            dp[n][k] = (f(n - 1, k - 1) + f(n - 1, k)) % 10007

    return dp[n][k]


n, k = map(int, input().split())
print(f(n, k))
