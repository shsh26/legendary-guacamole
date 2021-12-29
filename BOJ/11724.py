# -*- coding: utf-8 -*-
"""연결 요소의 개수

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

첫째 줄에 연결 요소의 개수를 출력한다.
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
check = [False] * n
ans = 0

for _ in range(m):
    u, v = map(lambda x: x - 1, map(int, input().split()))
    graph[u][v] = graph[v][u] = 1


def dfs(now: int):
    for nxt in range(n):
        if not check[nxt] and graph[now][nxt]:
            check[nxt] = True
            dfs(nxt)


def bfs(now: int):
    queue = deque()
    check[now] = True
    queue.append(now)

    while queue:
        nxt = queue.popleft()
        for i in range(n):
            if not check[i] and graph[nxt][i]:
                queue.append(i)
                check[i] = True


for i in range(n):
    if check[i]:
        continue
    bfs(i)
    ans += 1


print(ans)
