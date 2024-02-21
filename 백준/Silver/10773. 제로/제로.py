import sys
input = sys.stdin.readline

K = int(input())
stack = []

for _ in range(K):
    call = int(input())

    if call == 0:
        stack.pop()
        continue

    stack.append(call)

print(sum(stack))
