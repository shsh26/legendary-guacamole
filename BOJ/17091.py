# -*- coding: utf-8 -*-
"""단어 시계

단어 시계는 시각을 단어를 이용해서 표현하는 시계이다. 다음은 몇 가지 예시이다.

5:00 → five o' clock
5:01 → one minute past five
5:10 → ten minutes past five
5:15 → quarter past five
5:28 → twenty eight minutes past five
5:30 → half past five
5:40 → twenty minutes to six
5:45 → quarter to six
5:47 → thirteen minutes to six
분 = 0이면 "o' clock"을 사용하고, 1 ≤ 분 ≤ 30은 "past"를, 30 < 분이면 "to" 를 사용한다.

시각이 주어졌을 때, 단어 시계에서 사용하는 표현으로 출력해보자.

입력
첫째 줄에 시를 나타내는 h(1 ≤ h ≤ 12), 둘째 줄에 분을 나타내는 m(0 ≤ m < 60)이 주어진다.

출력
첫째 줄에 입력으로 주어진 시각을 단어 시계에서 사용하는 표현으로 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
import sys

inputs = sys.stdin.readline

HOURS = [
    "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve", "one"
]
MINUTES = [
    "", "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
    "eighteen", "nineteen", "twenty"
]


def get_fractions(hour: int, minute: int, tense: str) -> str:
    if minute == 1:
        return " ".join([HOURS[minute], "minute", tense, HOURS[hour]])
    elif minute == 15:
        return " ".join(["quarter", tense, HOURS[hour]])
    elif minute == 30:
        return " ".join(["half", tense, HOURS[hour]])
    elif 20 < minute < 30:
        return " ".join([MINUTES[20], MINUTES[minute % 10], "minutes", tense, HOURS[hour]])
    else:
        return " ".join([MINUTES[minute], "minutes", tense, HOURS[hour]])


def converts_number_to_word(hour: int, minute: int) -> str:
    if minute == 0:
        return " ".join([HOURS[hour], "o'", "clock"])
    elif minute <= 30:
        hour -= 1
        return get_fractions(hour, minute, "past")
    else:
        return get_fractions(hour, abs(60-minute), "to")


if __name__ == "__main__":
    h = int(inputs())
    m = int(inputs())

    print(converts_number_to_word(h, m))

