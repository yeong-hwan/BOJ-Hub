N = int(input())
prev, curr = 1, 1

for i in range(2, N+1):
    curr, prev = (curr + prev) % 15746, curr % 15746

print(curr)