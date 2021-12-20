# -*- coding: utf-8 -*-
"""수들의 합

서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

첫째 줄에 자연수 N의 최댓값을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
# 최대한 많은 서로 다른 자연수를 합해야 하므로 1부터 시작
s = int(input())

i = 0
while s * 2 > i * (i + 1):
    i += 1
print(i - 1)
