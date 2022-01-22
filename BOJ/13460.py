N, M = map(int, input().split())
board = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

red = ()
blue = ()

for i in range(N):
    char = input()
    for j in range(M):
        if char[j] == 'R':
            red = (i, j)
        elif char[j] == 'B':
            blue = (i, j)
        board.append(char[j])

print(board)
print(f'red: {red}')
print(f'blue: {blue}')


