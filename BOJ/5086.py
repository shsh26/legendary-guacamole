# -*- coding: utf-8 -*-
"""배수와 약수

4 × 3 = 12이다.

이 식을 통해 다음과 같은 사실을 알 수 있다.

3은 12의 약수이고, 12는 3의 배수이다.

4도 12의 약수이고, 12는 4의 배수이다.

두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다.
마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

1 2 3 3 4
1 3
"""


def solution(n: int, m: int):
    if m % n == 0:
        return "factor"
    elif n % m == 0:
        return "multiple"
    else:
        return "neither"


def short_code():
    """숏 코드
    """
    a = 1
    while a: a, b = map(int, input().split());a > 0 == print({0: "neither", b % a: "factor", 1: "multiple"}[a % b < 1])


if __name__ == '__main__':
    while True:
        a, b = map(int, input().split())
        if a==0 and b==0:
            break
        print(solution(a, b))

