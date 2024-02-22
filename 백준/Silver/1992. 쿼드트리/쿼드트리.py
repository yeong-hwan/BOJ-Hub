import sys
input = sys.stdin.readline

N = int(input())
video = [list(map(int, input().rstrip())) for _ in range(N)]

def check(paper):
    if len(paper) == 1:
        return True
    else:
        temp = paper[0][0]
        for row in paper:
            for col in row:
                if temp != col:
                    return False
        
        return True

def quad_tree(block, n):
    if check(block):
        if block[0][0] == 1:
            return 1
        else:
            return 0
    else:
        n = n // 2

        block_1 = [line[:n] for line in block[:n]]
        block_2 = [line[n:] for line in block[:n]]
        block_3 = [line[:n] for line in block[n:]]
        block_4 = [line[n:] for line in block[n:]]

        # print(block_1)
        # print(block_2)
        # print(block_3)
        # print(block_4)

        return f"({quad_tree(block_1, n)}{quad_tree(block_2, n)}{quad_tree(block_3, n)}{quad_tree(block_4, n)})"

answer = quad_tree(video, N)
print(answer)