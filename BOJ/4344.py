# -*- coding: utf-8 -*-
"""평균은 넘겠지

첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다
학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다.

점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(scores: list):

    result = 0
    avg = sum(scores[1:]) // scores[0]
    for s in scores[1:]:
        if s > avg:
            result += 1
    result = result / scores[0] * 100
    return result


def short_code():
    """숏 코드
    n = 학생 수
    s = 평균
    점수가 s 보다 크면 sum(True:1)
    """
    for T in range(int(input())):n,*l=map(int,input().split());s=sum(l)/n;print('%.3f%%'%(sum(i>s for i in l)*100/n))


if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(f'{solution(list(map(int, input().split()))):.3f}%')

    # short_code()
