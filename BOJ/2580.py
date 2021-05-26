# -*- coding: utf-8 -*-
"""N-Queen

가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데,
게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

나머지 빈 칸을 채우는 방식은 다음과 같다.
1. 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.

게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때
모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다.
스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.
스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


class Sudoku:
    def __init__(self):
        self._board = [list(map(int, input().split())) for _ in range(9)]
        self._zeros = [(i, j) for i in range(9) for j in range(9) if self._board[i][j] == 0]
        self._flag = False

    def is_promising(self, i, j):
        promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for k in range(9):
            if self._board[i][k] in promising:
                promising.remove(self._board[i][k])
            if self._board[k][j] in promising:
                promising.remove(self._board[k][j])

        i //= 3
        j //= 3

        for p in range(i * 3, (i + 1) * 3):
            for q in range(j * 3, (j + 1) * 3):
                if self._board[p][q] in promising:
                    promising.remove(self._board[p][q])

        return promising

    def dfs(self, x):
        if self._flag:
            return

        if x == len(self._zeros):
            for row in self._board:
                print(*row)
            self._flag = True
            return
        else:
            (i, j) = self._zeros[x]
            promising = self.is_promising(i, j)

            for num in promising:
                self._board[i][j] = num
                self.dfs(x + 1)
                self._board[i][j] = 0


if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.dfs(0)
