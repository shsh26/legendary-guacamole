# -*- coding: utf-8 -*-
"""큰 수의 법칙

다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
배열의 크기 M, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

Example:
    def solution((n: int, m: int, k: int, arr: List[int]):
        result = n
        return result

    if __name__ == '__main__':

        solution()

"""
from typing import List


# def solution(n: int, m: int, k: int, arr: List[int]):
#     """
#
#     Args:
#         n: 2 <= n <= 1000
#         m: 1 <= m <= 10000
#         k: 1 <= k <= 10000
#         arr: 다양한 수로 이루어진 배열 (n개)
#
#     Returns:
#         큰 수의 법칙에 따라 더해진 답
#     """
#     arr.sort()
#
#     first = arr[n - 1]
#     second = arr[n - 2]
#
#     result = 0
#
#     while True:
#         for i in range(k):
#             if m == 0:
#                 break
#             result += first
#             m -= 1
#         if m == 0:
#             break
#         result += second
#         m -= 1
#     return result

def solution(n: int, m: int, k: int, arr: List[int]):
    """

    Args:
        n: 2 <= n <= 1000
        m: 1 <= m <= 10000
        k: 1 <= k <= 10000
        arr: 다양한 수로 이루어진 배열 (n개)

    Returns:
        큰 수의 법칙에 따라 더해진 답
    """
    arr.sort()

    first = arr[n - 1]
    second = arr[n - 2]

    # int(m / (k + 1)) : 수열이 반복되는 횟수
    # * k = 수열 안에 가장 큰 수의 갯수(반복 횟수)
    count = int(m / (k + 1)) * k
    # 나누어 떨어지지 않는 경우 추가로 가장 큰 수가 더해지는 횟수
    count += m % (k + 1)

    result = 0
    result += count * first
    result += (m - count) * second
    return result


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solution(n, m, k, arr))
