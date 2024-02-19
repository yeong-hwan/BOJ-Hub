dp = [[[0]*(21) for _ in range(21)] for _ in range(21)] 
dp[0][0][0] = 1

def w(a, b, c):
    global dp
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    dp_now = dp[a][b][c]
    if dp_now != 0:
        return dp_now
    
    elif a < b and b < c:
        result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        dp[a][b][c] = result
        return result
    else:
        result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        dp[a][b][c] = result

        return result


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    result = 0
    if a <= 0 or b <= 0 or c <= 0:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = w(20, 20, 20)
    else:
        result = w(a, b, c)

    print(f'w({a}, {b}, {c}) = {result}')

# print(dp)