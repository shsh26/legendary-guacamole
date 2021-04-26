# -*- coding: utf-8 -*-
"""한수

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.

N이 주어졌을 때,
1보다 크거나 같고,
N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def detect(n: int):
    num = str(n)
    dis = 10
    for i in range(0, len(num)-1):
        if dis == 10:
            dis = int(num[i]) - int(num[i + 1])
        if dis != 10 and dis != int(num[i]) - int(num[i + 1]):
            return False
    return True


def solution(limit: int):
    if limit < 100:
        return limit
    r = range(1, limit+1)
    cnt = 0
    for i in r:
        if detect(i):
            cnt += 1
    return cnt


def short_code():
    """숏 코드
    숫자 i가 100 보다 작거나
    - i < 100
    1의 자리수와 100의 자리수의 합이 10의 자리수의 2배인 경우
    - i%10+i//100 == i//10%10*2
    +1을 한다.
    """
    print(sum(i<100 or i//10%10*2==i%10+i//100 for i in range(1,int(input())+1)))


if __name__ == '__main__':
    # print(solution(int(input())))
    short_code()
