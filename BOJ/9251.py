# -*- coding: utf-8 -*-
"""LCS

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
import sys


def solution(str1: str, str2: str):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


def short_code():
    """숏 코드
    """
    a = input()
    b = input()
    T = [0] * 300
    row = 0
    X = 0
    al = len(a)
    bl = len(b)
    for i in range(al):
        T[ord(a[i])] += (2 ** i)
    for i in range(al):
        if (a[i] == b[0]):
            row += (2 ** i)
            break
    for i in range(1, bl):
        X = T[ord(b[i])] | row
        row = X & ((X - (row * 2 + 1)) ^ X)

    cnt = 0
    while (row):
        cnt += (row % 2)
        row //= 2

    print(cnt)


if __name__ == '__main__':
    scan = sys.stdin.readline
    print(solution(scan().strip().upper(), scan().strip().upper()))
