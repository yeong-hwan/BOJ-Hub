import sys
input = sys.stdin.readline

def check_zero_count(row):
    lamps = list(row)
    zero_count = lamps.count('0')

    return zero_count


N, M = map(int, input().split())
table = [input().rstrip() for _ in range(N)]
K = int(input())

lamp_dict = {}

for row in table:
    lamp_dict[row] = 0

for row in table:
    lamp_dict[row] += 1

# print(lamp_dict)

result = 0

for key, value in lamp_dict.items():
    # print(key, value)
    zero_count = check_zero_count(key)

    if zero_count > K:
        continue

    if zero_count % 2 != K % 2:
        continue
    
    result = max(result, value)

print(result)
