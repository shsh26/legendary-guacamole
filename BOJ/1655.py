# -*- coding: utf-8 -*-
"""가운데를 말해요
"""
import sys
import heapq

input = sys.stdin.readline

N = int(input())

lheap, rheap = list(), list()
answer = list()

for _ in range(N):
    x = int(input())

    if len(lheap) == len(rheap):
        heapq.heappush(lheap, (-x, x))
    else:
        heapq.heappush(rheap, (x, x))

    if rheap and lheap[0][1] > rheap[0][0]:
        min_value = heapq.heappop(rheap)[0]
        max_value = heapq.heappop(lheap)[1]
        heapq.heappush(lheap, (-min_value, min_value))
        heapq.heappush(rheap, (max_value, max_value))

    answer.append(lheap[0][1])

for i in answer:
    print(i)
