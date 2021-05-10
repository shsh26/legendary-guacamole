# -*- coding: utf-8 -*-
"""체스판 다시 칠하기

MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드가 있다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서,
8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(board: list):
    chess = [[' '] * 8 for i in range(8)]

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                chess[i][j] = 'B'
            else:
                chess[i][j] = 'W'

    change = []
    for i in range(len(board[0]) - 7):
        for j in range(len(board) - 7):
            n = 0
            for k in range(8):
                for l in range(8):
                    if board[i + k][j + l] == chess[k][l]:
                        n = n + 1
    change.append(min(n, 64 - n))
    print(min(change))


def short_code():
    """숏 코드
    """
    l = [];exec('l.append(input().split());' * int(input()))
    print(*[sum(c > a and b < d for c, d in l) + 1 for a, b in l])


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [input() for i in range(n)]
    solution(board)