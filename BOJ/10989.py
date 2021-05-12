# -*- coding: utf-8 -*-
"""수 정렬하기 3

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: list):
    count = [0] * 10001
    count_sum = [0] * 10001
    for i in n:
        count[i] += 1

    count_sum[0] = count[0]

    for i in range(1, len(count)):
        count_sum[i] = count[i] + count_sum[i - 1]

    result = [0] * (len(n) + 1)

    for i in range(len(n) - 1, -1, -1):
        result[count_sum[n[i]]] = n[i]
        count_sum[n[i]] -= 1
    return result[1:]


def short_code():
    """숏 코드
    """


if __name__ == '__main__':
    for i in solution([int(input()) for i in range(int(input()))]):
        print(i)
