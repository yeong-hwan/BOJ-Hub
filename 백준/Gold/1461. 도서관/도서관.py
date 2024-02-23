from collections import deque
N, M = map(int, input().split())
result = 0

books = list(map(int, input().split()))
books.sort()

sorted_books = deque()
while books:
    sorted_books.appendleft(books.pop())

last = 0
result = 0

# print(sorted_books)

# left
if abs(sorted_books[0]) > abs(sorted_books[-1]):
    result += abs(sorted_books[0])
    for _ in range(M):
        if len(sorted_books) == 0:
            break
        if sorted_books[0] > 0:
            break
        sorted_books.popleft()
# right
else:  
    result += abs(sorted_books[-1])
    for _ in range(M):
        if len(sorted_books) == 0:
            break
        if sorted_books[-1] < 0:
            break
        sorted_books.pop()

# print(sorted_books)

left = deque()
right = deque()

while sorted_books:
    book = sorted_books.popleft()
    if book < 0:
        left.append(book)
    else:
        right.append(book)

# print(left, right)

while left:
    result += abs(left[0]) * 2
    for _ in range(M):
        if len(left) == 0:
            break
        left.popleft()

while right:
    result += abs(right[-1]) * 2
    for _ in range(M):
        if len(right) == 0:
            break
        right.pop()


print(result)