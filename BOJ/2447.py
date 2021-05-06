# -*- coding: utf-8 -*-
"""별 찍기 - 10

재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다

첫째 줄부터 N번째 줄까지 별을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def concatenate(r1: list, r2: list):
    return [''.join(x) for x in zip(r1, r2, r1)]


def solution(n: int):
    if n == 1:
        return ['*']
    n //= 3
    x = solution(n)
    a = concatenate(x, x)
    b = concatenate(x, [' ' * n] * n)

    return a + b + a


def star(n):
    if n == 3:
        return [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
    x = [[0] * n for i in range(n)]
    a = star(n // 3)
    for i in range(n):
        for j in range(n):
            if i // (n // 3) == j // (n // 3) == 1:
                x[i][j] = ' '
            else:
                x[i][j] = a[i % (n // 3)][j % (n // 3)]
    return x


def short_code():
    """숏 코드
    """
    n = int(input())
    s = '*'
    while n > 1:
        t = [i * 3 for i in s]
        s = t + [i + ' ' * len(i) + i for i in s] + t
        n //= 3
    print('\n'.join(s))


if __name__ == '__main__':
    n = int(input())
    a = star(n)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end='')
        print()
    ########################################
    print('\n'.join(solution(int(input()))))
