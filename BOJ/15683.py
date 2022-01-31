# -*- coding: utf-8 -*-
"""감시
"""
from copy import deepcopy

N, M = map(int, input().split())
room = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]
cctv = []
ans = 100

for i in range(N):
    line = list(map(int, input().split()))
    room.append(line)
    for j in range(M):
        if 0 < line[j] < 6:
            cctv.append([line[j], i, j])


def fill(maps, num, r, c):
    for i in num:
        nr = r
        nc = c
        while True:
            nr += dx[i]
            nc += dy[i]

            if not (0 <= nr < N and 0 <= nc < M):
                break
            if maps[nr][nc] == 6:
                break
            elif maps[nr][nc] == 0:
                maps[nr][nc] = 7


def dfs(depth, board):
    global ans
    if depth == len(cctv):
        count = 0
        for i in range(N):
            count += board[i].count(0)
        ans = min(ans, count)
        return
    temp = deepcopy(board)
    cc_num, cr, cc = cctv[depth]
    for i in cctv_direction[cc_num]:
        fill(temp, i, cr, cc)
        dfs(depth + 1, temp)
        temp = deepcopy(board)


dfs(0, room)
print(ans)
