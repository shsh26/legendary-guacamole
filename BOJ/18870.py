# -*- coding: utf-8 -*-
"""좌표 압축

수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(points: list):
    sorting = sorted(set(points), reverse=True)
    d = dict()
    l = len(sorting)
    for i in range(l):
        d[sorting[i]] = l - i-1
    for i in points:
        print(d[i], end=' ')
    return sorting


def short_code():
    """숏 코드
    """
    input()
    i = [*map(int, input().split())]
    a = dict(zip(sorted({*i}), range(9 ** 9)))
    print(*(a[x] for x in i))


if __name__ == '__main__':
    n, x = open(0)
    solution(list(map(int, x.split())))
