# -*- coding: utf-8 -*-
"""테트로미노
"""
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0
max_value = max(map(max, board))


def dfs(x, y, depth, total):
    global ans
    if ans >= total + max_value * (3 - depth):
        return
    if depth == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if depth == 1:
                    visited[nx][ny] = True
                    dfs(x, y, depth + 1, total + board[nx][ny])
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, total + board[nx][ny])
                visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, board[i][j])
        visited[i][j] = False

print(ans)
