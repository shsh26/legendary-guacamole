# -*- coding: utf-8 -*-
"""리모컨
"""
import sys

inputs = sys.stdin.readline

n = int(inputs())
m = int(inputs())
if m != 0:
    buttons = inputs().split()
else:
    buttons = []
ans = abs(n - 100)

for i in range(999999):
    check = True
    for j in str(i):
        if j in buttons:
            check = False
    if not check:
        continue

    cnt = len(str(i)) + abs(n - i)
    ans = min(ans, cnt)

print(ans)
