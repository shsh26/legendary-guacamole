# -*- coding: utf-8 -*-
"""크로아티아 알파벳

크로아티아 알파벳 	│  변경
č 	            │  c=
ć 	            │  c-
dž 	            │  dz=
đ 	            │  d-
lj 	            │  lj
nj 	            │  nj
š 	            │  s=
ž 	            │  z=

단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다.
위 목록에 없는 알파벳은 한 글자씩 센다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


def solution(string: str):
    for cro in alpha:
        string = string.replace(cro, 'a')
    return len(string)


def short_code():
    """숏 코드
    -, =, nj, lj, dz= 입력 단어에서 카운트
    전체 문자 수 -
    """
    c=input().count;print(c('')+~sum(map(c,'- = nj lj dz='.split())))


if __name__ == '__main__':
    print(solution(input()))
    # short_code()
