# -*- coding: utf-8 -*-
"""설탕배달

상근이는 요즘 설탕공장에서 설탕을 배달하고 있다.
상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,
5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
n = int(input())


def solution1(n: int):
    ans = n // 5 + n // 3 + 2
    for i in range(n // 5 + 1):
        for j in range(n // 3 + 1):
            if n == (5 * i) + (3 * j):
                ans = min(ans, i + j)
    if ans == n // 5 + n // 3 + 2:
        return(-1)
    return ans


def solution2(n: int):
    i = n
    cnt5 = 0
    cnt3 = 0
    if n < 3 or n == 4 or n == 7:
        ans = -1
    else:
        while i > 0:
            if i % 5 == 0:
                cnt5 += 1
            if i < 5:
                cnt5 = 0
                cnt3 += 1
                i = n - (cnt3 * 3) + 5
            i -= 5
        ans = cnt5 + cnt3
    return ans


print(solution1(n))
print(solution2(n))
