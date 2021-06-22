# -*- coding: utf-8 -*-
"""전깃줄

두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다.
합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

전깃줄이 연결되어 있는 경우 A의 1번 위치와 B의 8번 위치를 잇는 전깃줄,
A의 3번 위치와 B의 9번 위치를 잇는 전깃줄,
A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다.

전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다.
전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때,
남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다.
둘째 줄부터 한 줄에 하나씩 전깃줄이 A 전봇대와 연결되는 위치의 번호와 B 전봇대와 연결되는 위치의 번호가 차례로 주어진다.
위치의 번호는 500 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(n: int, pole: list):
    pole.sort(key=lambda x: x[0])

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if pole[j][1] < pole[i][1]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
    return n - max(dp)


def short_code():
    """숏 코드
    """
    n = int(input())
    d = {}
    for i in "A" * n: a, b = map(int, input().split());d[a] = b
    a = sorted(d.items())
    b = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j][1] < a[i][1]: b[i] = max(b[i], b[j] + 1)
    print(n - max(b))


if __name__ == '__main__':
    n = int(input())
    print(solution(n, [tuple(map(int, input().split())) for _ in range(n)]))
