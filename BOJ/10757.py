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
    입력한 두 수 더하기
    """
    print(sum(map(int, input().split())))


if __name__ == '__main__':
    print(sum(map(int, input().split())))