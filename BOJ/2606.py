# -*- coding: utf-8 -*-
"""바이러스
"""
from collections import deque

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(m):
    x, y = map(lambda v: v - 1, map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


def bfs():
    cnt = 0
    q = deque()
    visited = [0] * n
    q.append(0)
    visited[0] = 1
    while q:
        x = q.popleft()

        for j in graph[x]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1
                cnt += 1
    return cnt


print(bfs())
