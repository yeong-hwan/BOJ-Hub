N = int(input())
pairs = [list(map(int, input().split())) for _ in range(N)]
pairs.sort(key=lambda x : (x[1], x[0]))

for pair in pairs:
    print(pair[0], pair[1])
    