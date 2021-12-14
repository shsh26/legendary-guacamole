# -*- coding: utf-8 -*-
""" 일곱 난쟁이

아홉 명의 난쟁이 중 진짜 일곱 난쟁이를 찾아라
진짜 일곱 난쟁이들의 키의 총합은 100이다.

아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며,
아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

"""
from itertools import combinations

heights = [int(input()) for _ in range(9)]

# combination 활용 방법
for combi in combinations(heights, 7):
    if sum(combi) == 100:
        for h in sorted(combi):
            print(h)
        break
