# -*- coding: utf-8 -*-
"""쉬운 계단 수

45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int):
    dp = [[0] * 10 for _ in range(n)]
    dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][1]
            elif j == 9:
                dp[i][j] = dp[i - 1][8]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    return sum(dp[n-1]) % 1000000000


def short_code():
    """숏 코드
    """
    a = b = c = d = e = 1
    for _ in range(int(input()) - 1): a, b, c, d, e = b, a + c, b + d, c + e, d + e
    print((a + 2 * (b + c + d + e)) % 10 ** 9)


if __name__ == '__main__':
    print(solution(int(input())))
