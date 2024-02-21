import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)

answer = 0
delay = 0

while times:
    time = times.pop()
    answer += (time + delay)
    delay += time

print(answer)