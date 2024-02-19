N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
while K:
    coin_now = coins.pop()
    if K < coin_now:
        continue
    count += K // coin_now
    K %= coin_now

print(count)