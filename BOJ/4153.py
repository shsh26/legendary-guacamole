# -*- coding: utf-8 -*-
"""직각삼각형

주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(x: int, y: int, z: int):
    side = sorted([x, y, z])
    if side[0] ** 2 + side[1] ** 2 == side[2] ** 2:
        return 'right'
    else:
        return 'wrong'


def short_code():
    """숏 코드
    입력 숫자를 정렬해 c에 가장 긴 변 저장
    직각삼각형이면 'wrriognhgt' 중 [1]부터 2칸 씩 출력해 right
    """
    for i in open(0): a, b, c = sorted(map(int, i.split()));print("wrriognhgt"[a * a + b * b == c * c:a * b:2])


if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        print(solution(a, b, c))
