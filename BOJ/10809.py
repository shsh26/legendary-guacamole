# -*- coding: utf-8 -*-
"""알파벳 찾기

알파벳 소문자로만 이루어진 단어 S가 주어진다.

각각의 알파벳에 대해서,
단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(word: str):
    result = []
    for i in range(97, 123):
        if chr(i) in word:
            result.append(word.find(chr(i)))
        else:
            result.append(-1)
    return result


def short_code():
    """숏 코드
    a = 97, z = 122
    a ~ z 까지의 맵 생성
    input string 의 find
    """
    print(*map(input().find,map(chr,range(97,123))))


if __name__ == '__main__':
    print(*solution(input()))
    # short_code()
