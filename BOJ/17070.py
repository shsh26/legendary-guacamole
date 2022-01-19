# -*- coding: utf-8 -*-


def is_can_move(x, y):
    if board[x + 1][y] == 1 or board[x][y + 1] == 1:
        return False
    else:
        return True


dx = [0, 1, 1]
dy = [1, 0, 1]
n = int(input())
ans = 0

board = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))


def dfs(v, x, y):
    global ans

    if x == y == n - 1:
        ans += 1
        return

    for i in range(3):
        if (v == 0 and i == 1) or (v == 1 and i == 0):
            continue
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
            continue

        if visited[nx][ny]:
            continue

        if i == 2 and not is_can_move(x, y):
            continue
        visited[nx][ny] = True
        dfs(i, nx, ny)
        visited[nx][ny] = False


dfs(0, 0, 1)
print(ans)
############################
import sys


def check(y, x, d):
    for direction in directions[d]:
        dy, dx = cos[direction]
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < n and not g[ny][nx]:
            if direction != 2:  # 대각선이 아니면
                dp[ny][nx][direction] += dp[y][x][d]
            else:  # 대각선이면
                if not g[ny - 1][nx] and not g[ny][nx - 1]:
                    dp[ny][nx][direction] += dp[y][x][d]


directions = {0: [0, 2], 1: [1, 2], 2: [0, 1, 2]}  # 가로(0) / 세로(1) / 대각선(2)
cos = {0: [0, 1], 1: [1, 0], 2: [1, 1]}  # (y, x)

n = int(sys.stdin.readline().strip())
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
g = []

for _ in range(n):
    g.append([int(x) for x in sys.stdin.readline().split()])

dp[0][1][0] = 1

for y in range(n):
    for x in range(n):
        for d in range(3):
            if dp[y][x][d] and not g[y][x]:
                check(y, x, d)

print(sum(dp[n - 1][n - 1]))
