# -*- coding: utf-8 -*-
"""가장 긴 증가하는 부분 수열

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int, a: list):
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    return max(dp)


def short_code():
    """숏 코드
    """
    input()
    d = {}
    for i in map(int, input().split()): d[sum(i > d[k] for k in d)] = i
    print(len(d))


if __name__ == '__main__':
    print(solution(int(input()), list(map(int, input().split()))))
