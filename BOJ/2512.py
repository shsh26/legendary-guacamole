n = int(input())
needs = list(map(int, input().split()))
low = 1
high = max(needs)
budget = int(input())
ans = 1


def is_can_budget(mid):
    return budget >= sum(min(need, mid) for need in needs)


while low <= high:
    mid = (low + high) // 2

    if is_can_budget(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)
