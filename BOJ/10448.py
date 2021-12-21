# -*- coding: utf-8 -*-
"""유레카 이론

삼각수 Tn(n ≥ 1)는 [그림]에서와 같이 기하학적으로 일정한 모양의 규칙을 갖는 점들의 모음으로 표현될 수 있다.

자연수 n에 대해 n ≥ 1의 삼각수 Tn는 명백한 공식이 있다.
Tn = 1 + 2 + 3 + ... + n = n(n+1)/2

자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 만들어라.
단, 3개의 삼각수가 모두 달라야 할 필요는 없다.

프로그램은 표준입력을 사용한다. 테스트케이스의 개수는 입력의 첫 번째 줄에 주어진다.
각 테스트케이스는 한 줄에 자연수 K (3 ≤ K ≤ 1,000)가 하나씩 포함되어있는 T개의 라인으로 구성되어있다.

프로그램은 표준출력을 사용한다. 각 테스트케이스에대해 정확히 한 라인을 출력한다.
만약 K가 정확히 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
from itertools import combinations_with_replacement

for _ in range(int(input())):
    n = int(input())
    i = 1
    l = []
    ans = 0
    while n * 2 > i * (i + 1):
        l.append(i * (i + 1) // 2)
        i += 1
    for s in map(sum, combinations_with_replacement(l, 3)):
        if s == n:
            ans = 1
    print(ans)

# short code
# 미리 만들어지는 수를 구해 놓는다.
import sys

input = sys.stdin.readline
t = int(input())
num = [0] * 1001
gauss = [n * (n + 1) // 2 for n in range(1, 46)]
for i in gauss:
    for j in gauss:
        for k in gauss:
            if i + j + k <= 1000:
                num[i + j + k] = 1
for i in range(t):
    print(num[int(input())])
