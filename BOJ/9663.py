# -*- coding: utf-8 -*-
"""N-Queen

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
n = int(input())
board = [0 for i in range(16)]
result = 0


def promising(dx: int):
    for i in range(dx):
        if board[dx] == board[i] or abs(board[dx] - board[i]) == dx - i:
            return False
    return True


def solution(dx: int):
    global result
    if dx > n:
        result += 1
    else:
        for i in range(1, n + 1):
            board[dx] = i
            if promising(dx):
                solution(dx + 1)


def short_code():
    """숏 코드
    """
    a = (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
    print(a[int(input())])


if __name__ == '__main__':
    solution(1)
    print(result)
