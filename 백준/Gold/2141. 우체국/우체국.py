import sys
input = sys.stdin.readline

N = int(input())

villages = [tuple(map(int, input().split())) for _ in range(N)]
villages.sort()

total_population = 0

for village in villages:
    total_population += village[1]

half_population = total_population / 2
# print(half_population)


temp_population = 0

for village in villages:
    temp_population += village[1]

    if temp_population >= half_population:
        print(village[0])
        break


