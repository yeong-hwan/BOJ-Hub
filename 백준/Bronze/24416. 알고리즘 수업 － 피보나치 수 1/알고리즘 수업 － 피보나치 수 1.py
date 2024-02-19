N = int(input())
recursion_count = 0
dp_count = 0

def fib(n):
    global dp_count
    curr, prev = 1, 1

    for step in range(3, n+1):
        dp_count += 1
        curr, prev = (curr + prev), curr
    
    return curr


recursion_count = fib(N)

print(recursion_count, dp_count)