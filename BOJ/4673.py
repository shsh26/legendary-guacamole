# -*- coding: utf-8 -*-
"""셀프 넘버

셀프 넘버는 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때,
이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.

n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고,
39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다.
예를 들어, 101은 생성자가 2개(91과 100) 있다.

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다.
1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

Another:
    self_number = [True] * 10001

    def d(n: int):
        ans = n
        while n > 0:
            ans += n % 10
            n //= 10
        return ans

    for i in range(1, 10001):
        index = d(i)
        if index < 10001:
            self_number[index] = False

    for i in range(1, 10001):
        if self_number[i]:
            print(i)

"""
from collections import defaultdict


def d(n: int) -> int:
    return n + sum(map(int, str(n)))


def solution(limit: int):
    # total = defaultdict(int)
    # for i in range(limit):
    #     if i > limit:
    #         break
    #     total[d(i)] += 1
    # for i in range(1, limit):
    #     if i not in total:
    #         print(i)
    total = range(limit)
    var = {*total} - {d(t) for t in total}
    return sorted(var)


def short_code():
    """숏 코드
    r = 9999까지의 Iterator
    """
    r=range(9999);print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))


if __name__ == '__main__':
    print(*solution(10000), sep="\n")

    # short_code()
