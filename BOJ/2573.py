# -*- coding: utf-8 -*-
"""빙산

빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당되는 칸에는 0이 저장된다.

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에,
배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
"""
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_coord(x, y):
    return 0 <= x < n and 0 <= y < m


def melt(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if arctic[nx][ny] == 0:
            count += 1
    return count


n, m = map(int, input().split())

arctic = [list(map(int, input().split())) for _ in range(n)]
year = 0


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    size = 1
    while q:
        sx, sy = q.popleft()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if is_coord(nx, ny) and not visited[nx][ny] and arctic[nx][ny] > 0:
                size += 1
                q.append([nx, ny])
                visited[nx][ny] = True

    return size


while True:

    visited = [[False] * m for _ in range(n)]
    arctic_temp = [[0] * m for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(m):
            if not visited[j][k] and arctic[j][k] > 0:
                cnt += 1
                bfs(j, k)

    if cnt >= 2:
        print(year)
        break
    if cnt == 0:
        print(0)
        break

    for j in range(n):
        for k in range(m):
            if arctic[j][k] > 0:
                arctic_temp[j][k] = arctic[j][k] - melt(j, k)
                if arctic_temp[j][k] < 0:
                    arctic_temp[j][k] = 0

    arctic = arctic_temp
    year += 1
