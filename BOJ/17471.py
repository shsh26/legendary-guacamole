# -*- coding: utf-8 -*-
from itertools import combinations
from collections import deque


def bfs(area):
    start = area[0]
    q = deque([start])
    visited = [0] * n
    visited[start] = 1
    sum_pop = 0
    while q:
        v = q.popleft()
        sum_pop += pop[v]
        for k in node[v]:
            if visited[k] == 0 and k in area:
                q.append(k)
                visited[k] = 1
    return sum_pop, sum(visited)


n = int(input())
pop = list(map(int, input().split()))
node = [[] for _ in range(n)]
ans = 10000

for i in range(n):
    _node = list(map(int, input().split()))
    for j in range(1, _node[0] + 1):
        node[i].append(_node[j] - 1)

for i in range(1, n // 2 + 1):
    for combi in combinations(range(n), i):
        a = list(combi)
        b = list(set(range(n)) - set(combi))
        sum_pop_a, a_visited = bfs(a)
        sum_pop_b, b_visited = bfs(b)

        if a_visited + b_visited == n:
            ans = min(ans, abs(sum_pop_a - sum_pop_b))

if ans != 10000:
    print(ans)
else:
    print(-1)

N = int(input())
peo = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for i in range(N):
    _, *edges = map(int, input().split())
    for j in edges:
        adj[i].append(j - 1)

red = []
blue = []
arr = []
checked = []
ans = 1000


def dfs(now):
    for nxt in adj[now]:
        if nxt in arr and not checked[nxt]:
            checked[nxt] = True
            dfs(nxt)


def is_possible():
    global arr, checked

    checked = [False] * N
    arr = red[:]
    checked[arr[0]] = True
    dfs(arr[0])
    for i in red:
        if not checked[i]:
            return False

    arr = blue[:]
    checked[arr[0]] = True
    dfs(arr[0])
    for i in blue:
        if not checked[i]:
            return False

    return True


for i in range(1, N // 2 + 1):
    for combi in combinations([i for i in range(N)], r):
        blue.clear()
        red = list(combi)
        for i in range(N):
            if i not in red:
                blue.append(i)

        if is_possible():
            ans = min(ans, abs(sum(peo[i] for i in red) - sum(peo[i] for i in blue)))


print(-1 if ans == 1000 else ans)
