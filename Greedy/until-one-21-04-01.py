# -*- coding: utf-8 -*-
"""1이 될 때까지

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하시오.

25 5
Example:
    def solution(n):
        result = n
        return result

    if __name__ == '__main__':
        N = map(int, input())
        solution(N)

"""


def solution(n: int, k: int):
    result = 0

    while True:
        temp = (n // k) * k
        result += n - temp
        n = temp
        if n < k:
            break
        result += 1
        n //= k
    result += (n - 1)
    return result


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solution(N, K))
