# -*- coding: utf-8 -*-
"""단어 공부

알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
from collections import Counter


def solution(word: str):
    if len(word) == 1:
        return word
    result = Counter(word).most_common(2)
    if result[0][1] == result[1][1]:
        return '?'
    else:
        return result[0][0]


def short_code():
    """숏 코드
    입력문자(대문자)에 대한 count
    a = 두번째로 많은 문자
    b = 첫번째로 많은 문자
    a < b 이면, -1
    a == b 이면, 0
    """
    s=input().upper();c=s.count;*_,a,b=v=sorted({*s,'?'},key=c);print(v[-(c(a)<c(b))])


if __name__ == '__main__':
    print(solution(input().upper()))
    # short_code()
