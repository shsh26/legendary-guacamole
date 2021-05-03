# -*- coding: utf-8 -*-
"""네 번째 점

세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

세 점의 좌표가 한 줄에 하나씩 주어진다.
죄표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

직사각형의 네 번째 점의 좌표를 출력한다.

Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution():
    x, y = list(), list()
    for i in range(3):
        _x, _y = map(int, input().split())
        x.append(_x)
        y.append(_y)

    re_x = x[2] if x[0] == x[1] else x[0] if x[1] == x[2] else x[1]
    re_y = y[2] if y[0] == y[1] else y[0] if y[1] == y[2] else y[1]
    print(f'{re_x} {re_y}')


def short_code():
    """숏 코드
    XOR 연산
    swap 함수
    """
    x = y = 0;
    exec("a,b=map(int,input().split());x^=a;y^=b;" * 3)
    print(x, y)


if __name__ == '__main__':
    solution()
    short_code()



