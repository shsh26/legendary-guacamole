from itertools import combinations
tc = 0
while True:

    k, *arr = map(int, input().split())
    if k == 0:
        break
    if tc:
        tc -= 1
        print()

    for combi in combinations(arr, 6):
        print(*combi)
    tc += 1