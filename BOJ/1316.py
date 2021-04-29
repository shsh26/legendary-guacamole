# -*- coding: utf-8 -*-
"""그룹 단어 체커

그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.

예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다.
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

첫째 줄에 그룹 단어의 개수를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(word: str):
    s = set(word)
    count = word.count

    for c in s:
        if c * count(c) not in word:
            return 0
    return 1


def short_code():
    """숏 코드
    첫 등장 문자를 기준으로 연속으로 나열한 것과 비교
    """
    print(sum([*x]==sorted(x,key=x.find)for x in open(0))-1)


if __name__ == '__main__':
    # print(sum(solution(input()) for i in range(int(input()))))
    # short_code()
    print(sorted("worddada", key="worddada".find))