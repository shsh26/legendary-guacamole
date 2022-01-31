# -*- coding: utf-8 -*-
"""로봇 청소기
"""
N, M = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def dfs(r, c, direct):
    global ans
    if maps[r][c] == 0:
        maps[r][c] = -1
        ans += 1
    for _ in range(4):
        nd = (direct + 3) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]

        if maps[nr][nc] == 0:
            dfs(nr, nc, nd)
            return
        direct = nd
    nd = (direct + 2) % 4
    nr = r + dr[nd]
    nc = c + dc[nd]
    if maps[nr][nc] == 1:
        return
    dfs(nr, nc, direct)


dfs(x, y, d)
print(ans)
