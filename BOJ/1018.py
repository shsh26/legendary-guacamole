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


def check_color(s_board: list):
    cnt = 0
    start = s_board[0][0]
    for i in range(8):
        for j in range(0, 8, 2):
            if s_board[i][j] != start:
                cnt += 1
            if s_board[i][j + 1] == start:
                cnt += 1
        if start == 'B':
            start = 'W'
        else:
            start = 'B'
    return cnt


def solution(board: list):
    result = []
    for i in range(len(board) - 7):
        for j in range(len(board[0]) - 7):
            cnt = check_color([x[j:j + 8] for x in board[i:i + 8]])
            result.append(min(cnt, 64 - cnt))
    return min(result)


def short_code():
    """숏 코드
    'B'와 'W'를 ord() 함수를 통해 정수로 변경
    각각 66과 87로 짝수와 홀수 -> 마지막 비트가 0과 1
    0 1 2 3 4 5 6 7
    b w b w b w b w = 0 0 0 0 0 0 0 0
    w b w b w b w b = 1 1 1 1 1 1 1 1
    각 행에서 0 또는 1로 통일(되어야 정상)
    따라서 행이 정상인 경우 4에서 빼는 경우 절대값이 4로 계산 되어야 한다.
    따라서 모든 값이 정상인 경우 32에서 구한 값의 절대값을 빼면 0이 된다.
    """
    N, M = map(int, input().split())
    r = range
    L = [[ord(c) + i + j & 1 for j, c in enumerate(input())] for i in r(N)]
    print(min(32 - abs(sum(4 - sum(l[j:j + 8]) for l in L[i:i + 8])) for i in r(N - 7) for j in r(M - 7)))


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solution([input() for i in range(n)]))
