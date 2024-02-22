import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

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

# 0~N-1
def dc(paper, n):
    global white
    global blue

    if check(paper):

        if paper[0][0] == 1:
            blue += 1
        else:
            white += 1
    
    else:
        paper_i = [line[:n//2] for line in paper[:n//2]]
        paper_ii = [line[n//2:] for line in paper[:n//2]]
        paper_iii = [line[:n//2] for line in paper[n//2:]]
        paper_iv = [line[n//2:] for line in paper[n//2:]]

        # print(paper_i)
        # print(paper_ii)
        # print(paper_iii)
        # print(paper_iv)
        
        global depth

        n = n // 2

        dc(paper_i, n)
        dc(paper_ii, n)
        dc(paper_iii, n)
        dc(paper_iv, n)
        

dc(paper, N)

print(white)
print(blue)

