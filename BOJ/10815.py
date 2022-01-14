import bisect

_ = int(input())
cards = sorted(list(map(int, input().split())))
_ = int(input())

result = []


def is_there(n):
    this = bisect.bisect_left(cards, n) - bisect.bisect_right(cards, n)
    if 0 != this:
        return 1
    else:
        return 0


for num in map(int, input().split()):
    result.append(is_there(num))

print(*result)
