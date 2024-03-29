R, C, Q = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(R)]
dp = [[0 for _ in range(C + 1)] for _ in range(R + 1)]


for i in range(1, R + 1):
    for j in range(1, C + 1):
        dp[i][j] = -dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1] + picture[i-1][j-1]

for i in range(Q):
    r1, c1, r2, c2 =  map(int, input().split())
    ans = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
    num = ((r2 - r1) + 1) * ((c2 - c1) + 1)
    print(ans // num)