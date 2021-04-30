# -*- coding: utf-8 -*-
"""큰 수 A+B

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


solution=sum


def short_code():
    """숏 코드
    첫 등장 문자를 기준으로 연속으로 나열한 것과 비교
    """
    print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)


if __name__ == '__main__':
    print(sum(map(int, input().split())))