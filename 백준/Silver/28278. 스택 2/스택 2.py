import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    order = list(map(int, input().split()))
    command = order[0]
    
    if command == 1:
        stack.append(order[1])
        continue

    if command == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        continue

    if command == 3:
        print(len(stack))
        continue

    if command == 4:
        if len(stack) == 0:
            print(1) 
        else:
            print(0)
        continue

    if command == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
