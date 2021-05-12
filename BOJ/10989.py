# -*- coding: utf-8 -*-
"""수 정렬하기 3

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
import sys


def solution():
    n = int(sys.stdin.readline())
    count = [0] * 10001
    for i in range(n):
        count[int(sys.stdin.readline())] += 1
    for i in range(10001):
        if count[i] != 0:
            for j in range(count[i]):
                print(i)


def short_code():
    """숏 코드
    """
    E = 5 ** 6
    l = [0] * E
    f = open(0)
    f.readline()
    for i in f: l[int(i)] += 1
    for i in range(E): print("%s\n" % i * l[i], end="")


if __name__ == '__main__':
    # solution()
    short_code()
