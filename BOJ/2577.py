# -*- coding: utf-8 -*-
"""숫자의 개수

세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에
0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

첫째 줄에 A,
둘째 줄에 B,
셋째 줄에 C가 주어진다.
A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.


Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(a: int, b: int, c: int):
    multi = str(a * b * c)

    result = []
    for idx in range(10):
        result.append(multi.count(str(idx)))
    return result


def short_code():
    """숏 코드

    n = 0, m = 1
    m * int(input()) 3번 반복
    전체 곱 m에서 0부터 9가 존재하는지 확인
    """
    exec('n,m=0,1' + '*int(input())' * 3 + ';print(str(m).count(str(n)));n+=1' * 10)


def other_solution():
    arr = [0] * 10

    A = int(input())
    B = int(input())
    C = int(input())

    multi = A * B * C

    while multi > 0:
        index = multi % 10
        arr[index] += 1
        multi //= 10

    for v in arr:
        print(v)


if __name__ == '__main__':
    A = int(input())
    B = int(input())
    C = int(input())
    for i in solution(A, B, C):
        print(i)
