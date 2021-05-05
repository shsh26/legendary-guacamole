# -*- coding: utf-8 -*-
"""팩토리얼

0보다 크거나 같은 정수 N이 주어진다.
이때, N!을 출력하는 프로그램을 작성하시오.

첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

첫째 줄에 N!을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
import math


def solution(n: int):
    return math.factorial(n)


def short_code():
    """숏 코드
    """
    a=b=1;exec('b*=a;a+=1;'*int(input()));print(b)


if __name__ == '__main__':
    print(solution(int(input())))
