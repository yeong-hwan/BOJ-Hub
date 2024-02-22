N = int(input())

extension_dict = dict()

for _ in range(N):
    name, extension = input().split(".")
    
    if extension not in extension_dict:
        extension_dict[extension] = 1
    else:
        extension_dict[extension] += 1

answer = sorted(extension_dict.items())

for pair in answer:
    print(*pair)