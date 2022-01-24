# -*- coding: utf-8 -*-
"""2048(Easy)
크기: N x N
최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하라.
"""
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0


def dfs(count, direct, before_board):
    global ans
    if count == 5:
        for l in before_board:
            ans = max(ans, max(l))
        return

    next_board = [[0] * N for _ in range(N)]

    line = list()
    line_sum = list()
    for i in range(N):
        line.clear()
        line_sum.clear()

        for j in range(N):
            if direct > 2:
                if before_board[j][i] != 0:
                    line.append(before_board[j][i])
            else:
                if before_board[i][j] != 0:
                    line.append(before_board[i][j])

        if direct == 1 or direct == 4:
            line.reverse()

        while line:
            if len(line) > 1 and line[0] == line[1]:
                line_sum.append(line.pop(0) * 2)
                line.pop(0)
            else:
                line_sum.append(line.pop(0))

        for j in range(len(line_sum)):
            if direct == 1:
                next_board[i][N - j - 1] = line_sum[j]
            elif direct == 4:
                next_board[N - j - 1][i] = line_sum[j]
            elif direct == 2:
                next_board[i][j] = line_sum[j]
            elif direct == 3:
                next_board[j][i] = line_sum[j]

    for i in range(1, 5):
        if next_board == before_board and i == direct:
            continue
        dfs(count + 1, i, next_board)


for d in range(1, 5):
    dfs(0, d, board)
print(ans)
