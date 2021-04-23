# -*- coding: utf-8 -*-
"""조이스틱

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.

조이스틱을 각 방향으로 움직이면 아래와 같습니다.
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동

예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.


Example:
    def solution(name: str):
        result = name
        return result

    if __name__ == '__main__':

        solution()

"""


def solution(name: str):
    name_len = len(name)
    min_move = name_len - 1
    result = 0
    for i in range(name_len):
        if ord(name[i]) <= ord('M'):
            result += ord(name[i]) - ord('A')
        else:
            result += ord('Z') - ord(name[i]) + 1

        next_str = i + 1
        while next_str < name_len and name[next_str] == 'A':
            next_str += 1
        min_move = min(min_move, i + name_len + min(i, name_len - next_str))

    result += min_move

    return result


if __name__ == '__main__':
    input_name = input()
    print(solution(input_name))
