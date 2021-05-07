# -*- coding: utf-8 -*-
"""하노이 탑 이동 순서

세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다.
각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
2. 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

첫째 줄에 옮긴 횟수 K를 출력한다.

두 번째 줄부터 수행 과정을 출력한다.
두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데,
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int, start: int, to: int, via: int):
    if n == 1:
        print(start, to)
        return 1
    else:
        solution(n-1, start, via, to)
        print(start, to)
        solution(n-1, via, to, start)


def short_code():
    """숏 코드
    """
    N = int(input())
    print(2 ** N - 1)

    def h(a, b, c, l):
        if l: h(a, c, b, l - 1);print(a, b);h(c, b, a, l - 1)

    h(1, 3, 2, N)


if __name__ == '__main__':
    n = int(input())
    print(2 ** n - 1)
    solution(n, 1, 3, 2)
