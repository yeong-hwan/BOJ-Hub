from collections import deque

N = int(input())
cards = deque()
for i in range(1, N+1):
    cards.append(i)

tricks = list(map(int, input().split()))
tricks = tricks[::-1]
result = deque()

for trick in tricks:
    if trick == 1:
        result.append(cards.popleft())
    elif trick == 2:
        result.insert(-1, cards.popleft())
    elif trick == 3:
        result.appendleft(cards.popleft())

result.reverse()

print(*result)