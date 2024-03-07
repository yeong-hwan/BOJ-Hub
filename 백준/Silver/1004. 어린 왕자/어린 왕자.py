import math
T = int(input())

for _ in range(T):
    result = 0

    start_x, start_y, departure_x, departure_y = map(int, input().split())
    num = int(input())

    for planet in range(num):
        x, y, distance = map(int, input().split())
        start_distance = math.sqrt( (start_x-x)**2 + (start_y-y)**2 )
        departure_distance = math.sqrt( (departure_x-x)**2 + (departure_y-y)**2 )

        if start_distance < distance and departure_distance < distance:
            continue
        if start_distance > distance and departure_distance > distance:
            continue
        
        result += 1
    
    print(result)