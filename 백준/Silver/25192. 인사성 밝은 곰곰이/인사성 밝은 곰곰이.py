N = int(input())

gomgom = set()
result = 0

for _ in range(N):
    log = input()

    if log == "ENTER":
        result += len(gomgom)
        gomgom = set()
        continue
    
    if log not in gomgom:
        gomgom.add(log)

result += len(gomgom)

print(result)