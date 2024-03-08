import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

S = input()

P = 'I'

for _ in range(N):
    P += "OI"

result = 0

for idx in range(M-len(P)+1):
    check = S[idx:idx+len(P)]
    if check == P:
        result += 1
    
print(result)
