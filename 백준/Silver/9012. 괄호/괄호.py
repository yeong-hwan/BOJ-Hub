import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = list(input().rstrip())
    ps = ps[::-1]
    vps_count = 0
    
    while ps:
        now = ps.pop()
        if now == "(":
            vps_count += 1
        elif now == ")":
            vps_count -= 1
        
        
        if vps_count < 0:
            break
    
    if vps_count == 0:
        print("YES")
    else:
        print('NO')
