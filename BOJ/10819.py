# -*- coding: utf-8 -*-
"""차이를 최대로
"""
from itertools import permutations

N = int(input())
a = list(map(int, input().split()))
ans = 0


def add_list(temp: tuple):
    return sum(abs(temp[i - 1] - temp[i]) for i in range(1, N))


for li in permutations(a, N):
    ans = max(ans, add_list(li))

print(ans)
