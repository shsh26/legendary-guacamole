for _ in range(int(input())):
    ps = input()
    l = list()
    for s in ps:
        if s == '(':
            l.append(s)
        else:
            if not l:
                print('NO')
                break
            l.pop()
    if l:
        print('NO')
    else:
        print('YES')