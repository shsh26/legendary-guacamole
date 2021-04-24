# -*- coding: utf-8 -*-
"""평균

점수 중에 최댓값을 M 이라고 한다. 모든 점수를 점수/M*100으로 계산한다.

성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

첫째 줄에 시험 본 과목의 개수 N이 주어진다.
이 값은 1000보다 작거나 같다.

둘째 줄에 현재 성적이 주어진다.
이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(numbers: list):
    m = max(numbers)
    result = 0
    for n in numbers:
        result += n / m * 100
    result = result / len(numbers)

    return result


def short_code():
    """숏 코드

    n = 과목 수
    a = 과목당 점수
    """
    result = sum(b := [*map(int, [*open(0)][1].split())]) * 100 / max(b) / len(b)
    print(result)


if __name__ == '__main__':
    # subject_num = int(input())
    # subject = list(map(int, input().split()))
    #
    # print(solution(subject))
    short_code()
