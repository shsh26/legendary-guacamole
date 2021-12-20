# -*- coding: utf-8 -*-
"""캠핑

캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다.
강산이는 이제 막 V일짜리 휴가를 시작했다. 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, L, P, V를 순서대로 포함하고 있다.
모든 입력 정수는 int범위이다. 마지막 줄에는 0이 3개 주어진다.

각 테스트 케이스에 대해서, 강산이가 캠핑장을 최대 며칠동안 사용할 수 있는지 예제 출력처럼 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
t = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    ans = l * (v // p)
    v -= (p * (v // p))
    ans += l if v > l else v
    print(f'Case {t}: {ans}')
    t += 1
