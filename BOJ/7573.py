# -*- coding: utf-8 -*-
"""고기잡이
"""
import sys

input = sys.stdin.readline

n, l, m = map(int, input().split())

fishes = [list(map(int, input().split())) for _ in range(m)]
fishes.sort()
ans = 0

for h in range(1, l // 2):
    w = l // 2 - h
    if w > n - 1 or h > n - 1:
        continue
    for i in range(m):
        y = fishes[i][0]
        x = fishes[i][1]

        for j in range(w + 1):
            cnt = 1
            for k in range(i + 1, m):
                ny = fishes[k][0]
                nx = fishes[k][1]
                if ny > y + h:
                    break
                if x - j <= nx <= x - j + w:
                    cnt += 1
            ans = max(ans, cnt)

print(ans)
