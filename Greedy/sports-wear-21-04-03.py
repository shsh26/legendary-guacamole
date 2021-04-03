# -*- coding: utf-8 -*-
"""체육복

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열이 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 구하세요.

Example:
    def solution(n: int, lost: int, reserve: List):
        result = n
        return result

    if __name__ == '__main__':

        solution()

"""
from typing import Iterator


def solution(n: int, lost: Iterator[int], reserve: Iterator[int]):
    r = [i for i in reserve if i not in lost]
    li = [j for j in lost if j not in reserve]

    for i in r:
        b = i - 1
        f = i + 1

        if b in li:
            li.remove(b)
        elif f in li:
            li.remove(f)
    return n - len(li)


if __name__ == '__main__':
    N = int(input())
    Lost = map(int, input().split())
    Reserve = map(int, input().split())

    solution(N, Lost, Reserve)
