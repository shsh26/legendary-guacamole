# -*- coding: utf-8 -*-
"""소트인사이드

배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(number: str):
    for i in sorted(number, reverse=True):
        print(i, end='')


def short_code():
    """숏 코드
    """
    print(*sorted(input())[::-1], sep='')


if __name__ == '__main__':
    solution(input())
    # short_code()
