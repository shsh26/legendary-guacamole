# -*- coding: utf-8 -*-
"""드래곤 커브
"""

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
N = int(input())
board = [[0] * 101 for _ in range(101)]

for i in range(N):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1
    temp = [d]
    q = [d]

    for _ in range(g + 1):
        for k in q:
            x += dx[k]
            y += dy[k]
            board[x][y] = 1
        q = [(i + 1) % 4 for i in temp]
        q.reverse()
        temp = temp + q

ans = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] == 1:
            ans += 1

print(ans)
