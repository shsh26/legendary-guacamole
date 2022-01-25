from collections import deque

N, K, M = map(int, input().split())

adj = [[] for _ in range(N + M)]
for i in range(M):
    for j in map(lambda x: x - 1, map(int, input().split())):
        adj[N + j].append(j)
        adj[j].append(N + j)


def bfs():
    check = [False] * (N + M)
    check[0] = True
    dq = deque()
    dq.append((0, 1))
    while dq:
        now, d = dq.popleft()
        if now == N - 1:
            return (d + 1) // 2
        nd = d + 1
        for nxt in adj[now]:
            if not check[nxt]:
                check[nxt] = True
                dq.append((nxt, nd))

    return -1
