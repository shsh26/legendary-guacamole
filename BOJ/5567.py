import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
board = [[] for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = 0

for _ in range(m):
    x, y = map(lambda x: x - 1, map(int, input().split()))
    board[x].append(y)
    board[y].append(x)


def bfs():
    global ans
    dq = deque()
    check = [0] * n
    check[0] = 1
    dq.append((0, 0))
    while dq:
        now, depth = dq.popleft()
        ans += 1

        if depth < 2:
            nd = depth + 1
            for nxt in board[now]:
                check[nxt] = 1
                dq.append((nxt, nd))
    return sum(check)


print(bfs() - 1)
