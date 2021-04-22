# -*- coding: utf-8 -*-
"""사분면 고르기

점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
단, x 좌표와 y 좌표는 모두 양수나 음수라고 가정한다.

첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0)
다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)


Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(x: int, y: int):
    if x > 0 and y > 0:
        return '1'
    if x < 0 < y:
        return '2'
    if x < 0 and y < 0:
        return '3'
    if x > 0 > y:
        return '4'


def short_code():
    """숏 코드

    open(0)으로 한 줄씩 입력
    '3421'에서
    a > 0: '41', True 에서 2칸 씩
    a < 0: '32', False 에서 2칸 씩
    True == 1, False == 0

    """
    a, b = map(int, open(0))
    print('3421'[a > 0::2][b > 0])


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    print(solution(x, y))
