N = int(input())
compare_group = set(map(int, input().split()))
M = int(input())
input_gorup = list(map(int, input().split()))

for number in input_gorup:
    if number in compare_group:
        print(1)
    else:
        print(0)