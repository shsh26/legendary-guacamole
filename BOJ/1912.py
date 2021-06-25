# -*- coding: utf-8 -*-
"""연속합

n개의 정수로 이루어진 임의의 수열이 주어진다.
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
여기서 정답은 12+21인 33이 정답이 된다.

첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

첫째 줄에 답을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

10 6 9
10-4 -4
6+3 3

"""


def solution(n: int, sequence: list):
    dp = [sequence[0]]

    for i in range(n - 1):
        dp.append(max(dp[i] + sequence[i + 1], sequence[i + 1]))
    return max(dp)


def short_code():
    """숏 코드
    """
    r = input
    r()
    g = m = -1e9
    for i in r().split(): g = max(g, 0) + int(i);m = max(m, g)
    print(m)


if __name__ == '__main__':
    n = int(input())
    print(solution(n, list(map(int, input().split()))))
