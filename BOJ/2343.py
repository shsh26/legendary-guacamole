# -*- coding: utf-8 -*-
"""기타 레슨
"""
n, m = map(int, input().split())

lec = list(map(int, input().split()))

low = max(lec)
high = sum(lec)

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    temp = 0

    for i in range(n):
        if temp + lec[i] > mid:
            temp = 0
            cnt += 1
        temp += lec[i]

    if temp != 0:
        cnt += 1

    if cnt <= m:
        high = mid - 1
    else:
        low = mid + 1

print(low)
