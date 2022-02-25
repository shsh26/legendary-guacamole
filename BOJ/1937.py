# -*- coding: utf-8 -*-
"""욕심쟁이 판다
"""
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
inputs = sys.stdin.readline

forest = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0


def bfs(x, y):
    q = deque()
    total = 0

    q.append([x, y])

    while q:
        sx, sy = q.popleft()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and forest[sx][sy] < forest[nx][ny]:
                q.append([nx, ny])
                total = max(total, len(q))

    return total


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


n = int(inputs())
dp = [[0] * n for _ in range(n)]

for _ in range(n):
    forest.append(list(map(int, inputs().split())))

for j in range(n):
    for k in range(n):
        ans = max(ans, dfs(j, k))

print(ans)
