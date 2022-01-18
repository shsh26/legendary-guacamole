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
