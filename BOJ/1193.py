# -*- coding: utf-8 -*-
"""분수찾기

무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…

이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

첫째 줄에 분수를 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

i번째 대각선에는 i개의 원소가 있다.
X가 존재하는 대각선은
홀수번째 대각선은 아래로 증가
짝수번째 대각선은 위로 증가

"""
n = int(input())
x = n


# solution #1
k = 1
b = 2

while n > k:
    k += b
    b += 1

if b % 2 == 0:
    col = k - n + 1
    row = b - 1 - (k - n)
else:
    col = b - 1 - (k - n)
    row = k - n + 1
print(f'{col}/{row}')


# solution #2
i = 1
while n > i:
    n -= i
    i += 1

if i % 2 == 0:
    print(f'{n}/{i + 1 - n}')
else:
    print(f'{i + 1 - n}/{n}')


# solution #3
i = 1
while x > i * (i + 1) // 2:
    i += 1

b = i * (i - 1) // 2
ans1 = i - x + b + 1
ans2 = i + 1 - ans1

if i % 2 == 0:
    print(f'{ans2}/{ans1}')
else:
    print(f'{ans1}/{ans2}')