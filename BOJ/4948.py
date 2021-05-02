# -*- coding: utf-8 -*-
"""베르트랑 공준

베르트랑 공준은 임의의 자연수 n에 대하여,
n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다.
(11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
입력의 마지막에는 0이 주어진다.

각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int):
    r = range(2 * n + 1)
    li = [1 for i in r]

    for i in r:
        if i < 2:
            li[i] = 0
            continue
        for j in range(i * 2, 2 * n + 1, i):
            li[j] = 0
    # return [i for i in range(1, 2*n+1) if all(i % j for j in range(2, int(i ** .5 + 1))) * i > 1]
    return li


def short_code():
    """숏 코드

    """
    m = 999999
    i, e = 1, [1] * (m + 1)
    while (i := i + 1) * i < m + 1:
        if e[i]: e[2 * i::i] = [0] * (m // i - 1)
    while (n := int(input())) > 0:
        print(sum(e[n + 1:2 * n + 1]))


if __name__ == '__main__':
    li = solution(123456)

    while True:
        n = int(input())
        if n == 0:
            break
        print(li[n + 1:2 * n + 1].count(1))
