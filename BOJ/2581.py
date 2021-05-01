# -*- coding: utf-8 -*-
"""소수

자연수 M과 N이 주어질 때,
M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들
소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우
60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
이들 소수의 합은 620이고, 최솟값은 61이 된다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(m: int, n: int):
    li = [i for i in range(n+1)]

    for i in li:
        if i < 2:
            li[i] = 0
            continue
        for j in range(i*2, n+1, i):
            li[j] = 0

    total = set(li[m:])
    if 0 in total:
        total.remove(0)

    if not total:
        print(-1)
    else:
        print(sum(total))
        print(min(total))


def short_code():
    """숏 코드
    m ~ n의 수를  2 ~ 루트 n + 1까지 나눠
    나머지가 0인 경우 거짓 -> all() -> 0 -> False
    나누어 떨어지지 않는 경우 참 -> all() -> 1 -> True
    """
    p = [n for n in range(int(input()), int(input()) + 1) if all(n % j for j in range(2, int(n ** .5 + 1))) * n > 1]
    print(p and f'{sum(p)}\n{min(p)}' or -1)


if __name__ == '__main__':
    # a = int(input())
    # b = int(input())
    # solution(a, b)
    short_code()
