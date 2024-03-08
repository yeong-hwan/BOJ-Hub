import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_listens = set()
no_sees = set()

for _ in range(N):
    no_listens.add(input().rstrip())

for _ in range(M):
    no_sees.add(input().rstrip())

# print(no_listens, no_sees)

result = sorted(list(no_listens & no_sees))

print(len(result))
for people in result:
    print(people)