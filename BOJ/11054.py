# -*- coding: utf-8 -*-
"""가장 긴 바이토닉 부분 수열

수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,
{1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int, a: list):
    u = [0] * n
    d = [0] * n
    ans = 0
    ur = range(n)
    dr = range(n-1, -1, -1)
    for ui, di in zip(ur, dr):
        for j in range(ui):
            if a[ui] > a[j] and u[ui] < u[j]:
                u[ui] = u[j]
        for k in range(n-1, di, -1):
            if a[di] > a[k] and d[di] < d[k]:
                d[di] = d[k]
        u[ui] += 1
        d[di] += 1

    for i in range(n):
        if ans < (u[i] + d[i] - 1):
            ans = u[i] + d[i] - 1
    return ans


def short_code():
    """숏 코드
    """
    n = int(input())
    A = list(map(int, input().split()))
    m = max(A)
    upDP = [0] * (m + 1)
    downDP = [0] * (m + 1)
    R = [0] * (n + 1)
    for i in range(n):
        upDP[A[i]] = max(upDP[:A[i]]) + 1
        downDP[A[n - i - 1]] = max(downDP[:A[n - i - 1]]) + 1
        R[i] += upDP[A[i]]
        R[n - i - 1] += downDP[A[n - i - 1]]
    print(max(R) - 1)


if __name__ == '__main__':
    print(solution(int(input()), list(map(int, input().split()))))
