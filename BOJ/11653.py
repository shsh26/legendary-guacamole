# -*- coding: utf-8 -*-
"""소인수분해

정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int):
    i = 2
    while n != 1:
        if n % i == 0:
            print(i)
            n /= i
        else:
            i += 1


def short_code():
    """숏 코드
    """
    N = int(input());
    a = 2
    while N > 1:
        if N % a:
            a += 1
        else:
            print(a);N /= a


if __name__ == '__main__':
    solution(int(input()))