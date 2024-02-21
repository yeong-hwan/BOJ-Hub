import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(reverse=True)

# print(meetings)

total_start, total_end = 0, 0
result = []

while meetings:
    now = meetings.pop()
    start, end = now
    if total_end <= start:
        total_end = end
        result.append(now)
    elif total_end > end:
        total_end = end
        result.pop()
        result.append(now)

print(len(result))