# -*- coding: utf-8 -*-
"""문자열 반복



문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고,
두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8),

문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(repeat: int, word: str):
    result = ''
    for c in word:
        result += c * repeat
    return result


def short_code():
    """숏 코드
    a = 97, z = 122
    a ~ z 까지의 맵 생성
    input string 의 find
    """
    for r,_,*s,_ in[*open(0)][1:]:print(''.join(c*int(r)for c in s))


if __name__ == '__main__':
    for t in range(int(input())):
        i, w = input().split()
        print(solution(int(i), w))
    # short_code()
