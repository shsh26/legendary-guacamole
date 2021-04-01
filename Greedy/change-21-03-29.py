# -*- coding: utf-8 -*-
"""거스름돈

거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 돈전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

Example:
    def solution(n):
        result = n
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int):
    count = 0
    coin_type = [500, 100, 50, 10]

    for coin in coin_type:
        count += n // coin
        n %= coin

    return count


if __name__ == '__main__':
    change = 1260
    print(solution(change))
