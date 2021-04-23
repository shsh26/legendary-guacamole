# -*- coding: utf-8 -*-
"""나머지

두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지이다.

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.


Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(numbers: list):
    num_set = set()
    for n in numbers:
        mod = n % 42
        num_set.add(mod)

    result = len(num_set)
    return result


def short_code():
    """숏 코드

    n = set()
    집합 n에 입력값의 나머지 42 add 10번 반복
    집합의 길이 출력
    """
    exec('n=set()' + ';n.add(int(input())%42)' * 10 + ';print(len(n));')


if __name__ == '__main__':
    # num_list = [int(input()) for i in range(10)]
    # print(solution(num_list))
    short_code()
