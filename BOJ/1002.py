# -*- coding: utf-8 -*-
"""터렛

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고,
조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다.
x1, y1, x2, y2는 -10,000보다 크거나 같고,
10,000보다 작거나 같은 정수이고,
r1, r2는 10,000보다 작거나 같은 자연수이다.

각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다.
만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

Example:
    def solution():
        result = do_something()
        return result

    if __name__ == '__main__':

        solution()

"""
import math


def solution(a: tuple, b: tuple):
    if a == b:
        return -1
    x = a[0] - b[0]
    y = a[1] - b[1]
    dis = math.sqrt((x**2) + (y**2))
    print(dis)
    if abs(a[2] - b[2]) < dis < a[2] + b[2]:
        return 2
    if abs(a[2]-b[2]) == dis or dis == a[2] + b[2]:
        return 1
    if abs(a[2]-b[2]) > dis or dis > a[2] + b[2]:
        return 0


def short_code():
    """숏 코드
    a = 두 중심 사이의 거리
    b, c = 각 원의 반지름의 제곱
    """
    exec('x,y,r,X,Y,R=map(int,input().split());a=(X-x)**2+(Y-y)**2;b=(R+r)**2;c=(R-r)**2;print([[1+(a!=b)*(a!=c),-1][a+c<1],0][a>b or a<c]);'*int(input()))


if __name__ == '__main__':
    for i in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(solution((x1, y1, r1), (x2, y2, r2)))
