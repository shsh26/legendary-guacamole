# -*- coding: utf-8 -*-
""" 사탕 게임

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

풀이 과정
1. 바꾸기
2. 출 찾기
3. 원상 복귀

"""
N = int(input())
board = [list(input()) for _ in range(N)]
ans = 1
# print(board)


def search():
    global ans

    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i - 1][j] == board[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j - 1] == board[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N):
        if j != N - 1:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            search()
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i != N - 1:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            search()
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(ans)