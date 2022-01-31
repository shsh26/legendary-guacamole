# -*- coding: utf-8 -*-
"""주사위 굴리기
"""
N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0] * 7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def roll(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
    elif direction == 4:
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]


for i in commands:
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < M:
        roll(i)
        if maps[nx][ny] != 0:
            dice[6] = maps[nx][ny]
            maps[nx][ny] = 0
        else:
            maps[nx][ny] = dice[6]
        print(dice[1])
        x += dx[i]
        y += dy[i]
