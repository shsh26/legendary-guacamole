# -*- coding: utf-8 -*-
import sys

inputs = sys.stdin.readline

whole = [list(map(int, inputs().split())) for _ in range(10)]
papers = [5, 5, 5, 5, 5]
result = set()


def check_size(y, x):
    length = 1
    for l in range(2, min(10 - y, 10 - x, 5) + 1):
        for i in range(y, y + l):
            for j in range(x, x + l):
                if whole[i][j] == 0:
                    return length
        length += 1
    return length


def fill(x, y, size, n):
    for _x in range(x, x + size):
        for _y in range(y, y + size):
            whole[_x][_y] = n


def backtracking(cnt):
    for i in range(0, 10):
        for j in range(0, 10):
            if whole[i][j] == 1:
                length = check_size(i, j)
                for l in range(length, 0, -1):
                    if papers[l - 1] > 0:
                        fill(i, j, l, 0)
                        papers[l - 1] -= 1
                        result.add(backtracking(cnt + 1))
                        fill(i, j, l, 1)
                        papers[l - 1] += 1
                if result:
                    return min(result)
                else:
                    return -1
    return cnt


result.add(backtracking(0))
if -1 in result:
    result.remove(-1)
print(min(result) if result else -1)


board = [list(map(int, input().split())) for _ in range(10)]
paper = [0] * 6
ans = 25


def is_possible(y, x, sz):
    if paper[sz] == 5 or y + sz > 10 or x + sz > 10:
        return False

    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False

    return True


def mark(y, x, sz, k):
    for i in range(sz):
        for j in range(sz):
            board[y + i][x + j] = k

    if k:
        paper[sz] -= 1
    else:
        paper[sz] += 1


def backtracking(y, x):
    global ans

    if y == 10:
        ans = min(ans, sum(paper))
        return

    if x == 10:
        backtracking(y + 1, 0)
        return

    if board[y][x] == 0:
        backtracking(y, x + 1)
        return

    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x + 1)
            mark(y, x, sz, 1)


backtracking(0, 0)
print(-1 if ans == 25 else ans)