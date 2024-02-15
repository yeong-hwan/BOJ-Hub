N = int(input())
coordinates = list(map(int, input().split()))

compare_sets = sorted(set(coordinates))

dic = {}

for idx in range(len(compare_sets)):
    dic[compare_sets[idx]] = idx

result = []

for coordinate in coordinates:
    result.append(dic[coordinate])

print(' '.join(str(x) for x in result))
