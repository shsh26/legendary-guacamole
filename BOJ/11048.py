n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i > 0:
            dp[i][j] = max(dp[i - 1][j], dp[i][j])
        if j > 0:
            dp[i][j] = max(dp[i][j - 1], dp[i][j])

        dp[i][j] += candies[i][j]

print(dp[n - 1][m - 1])
