import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

BLANK = '.'
colors = ['R', 'G', 'B', 'P', 'Y']

def bfs(height, width, color):
    count = 1
    block = [(height, width)]
    queue.append((height, width))

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < HEIGHT and 0 <= nx < WIDTH:
                if field[ny][nx] == color:
                    if visited[ny][nx] == False:
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        block.append((ny, nx))
                        count += 1

    if count >= 4:
        return block

def fill(block):
    for coordinate in block:
        y, x = coordinate
        for ny in range(y, 0, -1):
            # print(ny)
            field[ny][x] = field[ny-1][x]
        field[0][x] = BLANK

# const
HEIGHT = 12
WIDTH = 6

field = [list(input().rstrip()) for _ in range(HEIGHT)]
visited = [[0] * WIDTH for _ in range(HEIGHT)]

chain_count = 0

# chain loop
while True:

    explode_count = 0
    visited = [[0] * WIDTH for _ in range(HEIGHT)]
    blocks = []
    # explosion loop(block check)
    for height in range(HEIGHT):
        for width in range(WIDTH):
            if field[height][width] == BLANK:
                continue
            
            for color in colors:
                if field[height][width] != color:
                    continue

                if visited[height][width] == False:
                    visited[height][width] = True

                    block = bfs(height, width, color)
                    if block is not None:
                        blocks.append(block) 

    explode_count = len(blocks)

    # fill
    for block in blocks:
        fill(block)

    if explode_count == 0:
        break;

    chain_count += 1

print(chain_count)