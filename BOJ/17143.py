# -*- coding: utf-8 -*-
"""낚시왕
Pypy3용
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

R, C, M = map(int, input().split())
spot = [[0] * C for _ in range(R)]
ans = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d == 1 or d == 2:
        s %= ((R - 1) * 2)
    else:
        s %= ((C - 1) * 2)
    spot[r - 1][c - 1] = [s, d - 1, z]

time = 0

while time < C:
    for i in range(R):
        if spot[i][time] != 0:
            ans += spot[i][time][2]
            spot[i][time] = 0
            break

    sharks = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if spot[i][j] == 0:
                continue

            new_sharks = spot[i][j]
            spot[i][j] = 0

            s, d, z = new_sharks
            r, c = i, j

            for _ in range(s):
                r += dx[d]
                c += dy[d]
                if 0 <= r < R and 0 <= c < C:
                    continue
                else:
                    if d == 0: d = 1
                    elif d == 1: d = 0
                    elif d == 2: d = 3
                    else: d = 2
                    r += dx[d]
                    c += dy[d]

            if sharks[r][c] != 0:
                if z > sharks[r][c][2]:
                    sharks[r][c] = [s, d, z]
            else:
                sharks[r][c] = [s, d, z]

    spot = sharks

    time += 1

print(ans)
