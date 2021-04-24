# -*- coding: utf-8 -*-
"""OX퀴즈

O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고,
길이가 0보다 크고 80보다 작은 문자열이 주어진다.

문자열은 O와 X 만으로 이루어져 있다.

Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def to_n(x: str):
    return len(x) * (len(x) + 1) // 2


def solution(quiz: str):
    quiz = quiz.split('X')
    result = 0
    for c in quiz:
        result += to_n(c)

    return result


def short_code():
    """숏 코드
    """


if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(solution(input()))

    # short_code()
