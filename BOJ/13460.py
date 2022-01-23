from collections import deque

N, M = map(int, input().split())
board = [[]] * N

checked = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

rx, ry, bx, by = 0, 0, 0, 0

for i in range(N):
    char = input()
    temp = []
    for j in range(M):
        if char[j] == 'R':
            rx, ry = i, j
        elif char[j] == 'B':
            bx, by = i, j
        temp.append(char[j])
    board[i] = temp


def move(x, y, di_x, di_y):
    cnt = 0
    flag = False
    while board[x + di_x][y + di_y] != '#':
        x += di_x
        y += di_y
        cnt += 1

        if board[x][y] == 'O':
            flag = True
            break
    return x, y, cnt, flag


def bfs():
    q = deque()
    q.append((rx, ry, bx, by, 1))
    checked[rx][ry][bx][by] = True

    while q:
        cur_rx, cur_ry, cur_bx, cur_by, depth = q.popleft()

        if depth > 10:
            break

        for k in range(4):

            nxt_rx, nxt_ry, r_cnt, is_red_hole = move(cur_rx, cur_ry, dx[k], dy[k])
            nxt_bx, nxt_by, b_cnt, is_blue_hole = move(cur_bx, cur_by, dx[k], dy[k])

            if is_blue_hole:
                continue

            if is_red_hole:
                return depth

            if nxt_rx == nxt_bx and nxt_ry == nxt_by:
                if r_cnt > b_cnt:
                    nxt_rx -= dx[k]
                    nxt_ry -= dy[k]
                else:
                    nxt_bx -= dx[k]
                    nxt_by -= dy[k]

            if not checked[nxt_rx][nxt_ry][nxt_bx][nxt_by]:
                checked[nxt_rx][nxt_ry][nxt_bx][nxt_by] = True
                q.append((nxt_rx, nxt_ry, nxt_bx, nxt_by, depth + 1))

    return -1


print(bfs())
