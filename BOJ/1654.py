# -*- coding: utf-8 -*-
"""랜선 자르기
"""
import sys

input = sys.stdin.readline


def divide_cable(length):
    return sum(map(lambda x: x // length, cables))


k, n = map(int, input().split())

cables = [int(input()) for _ in range(k)]

low, high = 1, max(cables)
ans = []

while low <= high:
    mid = (low + high) // 2

    if n <= divide_cable(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)
