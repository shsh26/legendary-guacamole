import sys

input = sys.stdin.readline

N, M = map(int, input().split())
needs = [int(input()) for _ in range(N)]

high = sum(needs)
low = max(needs)
mid = (low + high) // 2
ans = high


def is_possible(k):
    money = 0
    cnt = 0
    for need in needs:
        if money < need:
            cnt += 1
            money = k - need
        else:
            money -= need
    return cnt <= M


while low <= high:
    if is_possible(mid):
        high = mid - 1
        ans = mid
    else:
        low = mid + 1
    mid = (low + high) // 2