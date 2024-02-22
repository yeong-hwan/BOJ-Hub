import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deck = deque()

for _ in range(N):
    command = input()
    integer = 0
    order = int(command[0])
    if order == 1:
        order, integer = command.split()
        deck.appendleft(integer)
        continue
    if order == 2:
        order, integer = command.split()
        deck.append(integer)
        continue
    elif order == 3:
        if len(deck) == 0:
            print(-1)
            continue
        print(deck.popleft())
    elif order == 4:
        if len(deck) == 0:
            print(-1)
            continue
        print(deck.pop())
    elif order == 5:
        print(len(deck))
    elif order == 6:
        if len(deck) == 0:
            print(1)
            continue
        print(0)
    elif order == 7:
        if len(deck) == 0:
            print(-1)
            continue
        now = deck.popleft()
        print(now)
        deck.appendleft(now)
    elif order == 8:
        if len(deck) == 0:
            print(-1)
            continue
        print(deck[-1])