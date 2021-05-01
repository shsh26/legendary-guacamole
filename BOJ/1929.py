# -*- coding: utf-8 -*-
"""소수 구하기

M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.

소수가 하나 이상 있는 입력만 주어진다.

Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(x: int, y: int):
    for i in range(x, y+1):
        if all(i % j for j in range(2, int(i ** .5 + 1))) * i > 1:
            print(i)


def short_code():
    """숏 코드

    """
    m, n = map(int, input().split());
    l = [*range(n + 1)]
    for i in l:
        if 1 < i: l[i * i::i] = -(i + ~n // i) * [0]
        if 1 < i >= m: print(i)


if __name__ == '__main__':
    x, y = map(int, input().split())
    solution(x, y)