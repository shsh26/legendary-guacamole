# -*- coding: utf-8 -*-
"""원판 돌리기
"""
import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# n, m, t = map(int, inputs().split())
#
# disks = [deque(map(int, inputs().split())) for _ in range(n)]
# rotate = [list(map(int, inputs().split())) for _ in range(t)]
#
# for tc in range(t):
#     x, d, k = rotate[tc]
#     result = 0
#
#     for i in range(n):
#         result += sum(disks[i])
#
#         if (i + 1) % x == 0:
#             if d == 0:
#                 disks[i].rotate(k)
#             else:
#                 disks[i].rotate(-k)
#
#     if result != 0:
#         remove = []
#
#         for i in range(n):
#             for j in range(m - 1):
#                 if disks[i][j] != 0 and disks[i][j + 1] != 0 and disks[i][j] == disks[i][j + 1]:
#                     remove.append((i, j))
#                     remove.append((i, j + 1))
#                 if disks[i][0] != 0 and disks[i][-1] != 0 and disks[i][0] == disks[i][-1]:
#                     remove.append((i, 0))
#                     remove.append((i, m - 1))
#
#         for j in range(m):
#             for i in range(n - 1):
#                 if disks[i][j] != 0 and disks[i + 1][j] != 0 and disks[i][j] == disks[i + 1][j]:
#                     remove.append((i, j))
#                     remove.append((i + 1, j))
#
#         remove = list(set(remove))
#
#         for i in range(len(remove)):
#             x, y = remove[i]
#             disks[x][y] = 0
#
#         if len(remove) == 0:
#             avg_sum = 0
#             zero_cnt = 0
#
#             for i in range(n):
#                 avg_sum += sum(disks[i])
#                 zero_cnt += disks[i].count(0)
#             avg = avg_sum / (n * m - zero_cnt)
#
#             for i in range(n):
#                 for j in range(m):
#                     if disks[i][j] != 0 and disks[i][j] > avg:
#                         disks[i][j] -= 1
#                     elif disks[i][j] != 0 and disks[i][j] < avg:
#                         disks[i][j] += 1
#         else:
#             break
#
# ans = 0
# for i in range(n):
#     ans += sum(disks[i])
#
# print(ans)


def bfs(x, y):
    q.append([x, y])
    xcnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0:
                ny = m - 1
            elif ny > m - 1:
                ny = 0

            if 0 <= nx < n and 0 <= ny < m and not c[nx][ny]:
                if a[x][y] == a[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
                    xcnt += 1

    return xcnt


n, m, t = map(int, input().split())

a, nsum, nm = [], 0, n * m
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    nsum += sum(row)

q = deque()
c = [[0] * m for _ in range(n)]

for _ in range(t):
    x, d, k = map(int, input().split())

    k %= m
    for i in range(x - 1, n, x):
        if d == 0:
            a[i] = a[i][-k:] + a[i][:-k]
            c[i] = c[i][-k:] + c[i][:-k]
        else:
            a[i] = a[i][k:] + a[i][:k]
            c[i] = c[i][k:] + c[i][:k]

    flag = 0
    for i in range(n):
        for j in range(m):
            if not c[i][j]:
                cnt = bfs(i, j)
                if cnt:
                    nsum -= a[i][j] * cnt
                    nm -= cnt
                    flag = 1

    if nm == 0:
        print(0)
        sys.exit()

    if not flag:
        avg = nsum / nm
        for i in range(n):
            for j in range(m):
                if not c[i][j]:
                    if a[i][j] > avg:
                        a[i][j] -= 1
                        nsum -= 1
                    elif a[i][j] < avg:
                        a[i][j] += 1
                        nsum += 1
print(nsum)
