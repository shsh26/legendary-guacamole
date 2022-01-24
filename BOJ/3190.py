# -*- coding: utf-8 -*-
"""뱀
"""
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
snake = deque()

for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

L = int(input())

move = []
for _ in range(L):
    t = input().split()
    move.append((int(t[0]), t[1]))

time = 0


def run():
    global time
    x, y = 0, 0
    d, cnt = 0, 0

    snake.append((x, y))
    board[x][y] = 2

    while True:
        time += 1
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 2:
            return
        elif board[nx][ny] == 0:
            board[nx][ny] = 2
            tail = snake.pop()
            board[tail[0]][tail[1]] = 0
            snake.appendleft((nx, ny))
        elif board[nx][ny] == 1:
            board[nx][ny] = 2
            snake.appendleft((nx, ny))

        if cnt < len(move):
            if time == move[cnt][0]:
                if move[cnt][1] == 'L':
                    d = (d + 1) % 4
                elif move[cnt][1] == 'D':
                    d = (d + 3) % 4
                cnt += 1

        x = nx
        y = ny


run()
print(time)
