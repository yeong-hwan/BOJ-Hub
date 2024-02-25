import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

R, C = map(int, input().split())
forest = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(destination):
    while queue:
        y, x = queue.popleft()

        destination_y, destination_x = destination
        if forest[destination_y][destination_x] == "S":
            return visited[destination_y][destination_x]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= ny < R and 0 <= nx < C:
                if (forest[ny][nx] == "." or forest[ny][nx] == "D") and forest[y][x] == "S":
                    forest[ny][nx] = "S"
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                    # print(visited)
                    
                elif (forest[ny][nx] == "." or forest[ny][nx] == "S") and forest[y][x] == "*":
                    forest[ny][nx] = "*"
                    queue.append((ny, nx))
        
    return "KAKTUS"

destination = []

for y in range(R):
    for x in range(C):
        if forest[y][x] == "S":
            queue.append((y, x))
        elif forest[y][x] == "D":
            destination = [y, x]

for y in range(R):
    for x in range(C):
        if forest[y][x] == "*":
            queue.append((y, x))

# print(destination)
# print(visited)

print(bfs(destination))