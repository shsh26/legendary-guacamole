# -*- coding: utf-8 -*-
"""다리 만들기
"""
from collections import deque

N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 99999
continent = 1


def bfs1(position, num: int):
    q = deque()
    q.append(position)
    maps[position[0]][position[1]] = num
    check[position[0]][position[1]] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 1 and not check[nx][ny]:
                check[nx][ny] = True
                maps[nx][ny] = num
                q.append([nx, ny])


def bfs2(num):
    global answer
    dist = [[-1] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if maps[i][j] == num:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if maps[nx][ny] > 0 and maps[nx][ny] != num:
                answer = min(answer, dist[x][y])
                return

            if maps[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])


for i in range(N):
    for j in range(N):
        if not check[i][j] and maps[i][j] == 1:
            bfs1([i, j], continent)
            continent += 1

for i in range(1, continent):
    bfs2(i)

print(answer)
