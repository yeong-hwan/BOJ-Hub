import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

answer = 0

if d > r1 + r2:
    answer = 0
elif d <= abs(r1 - r2):
    answer = math.pi * min(r1, r2)**2
else:
    p = (math.acos((r1**2 + (d * d) - r2**2) / (2 * r1 * d))) * 2
    t = (math.acos((r2**2 + (d * d) - r1**2) / (2 * r2 * d))) * 2
    a1 = 0.5 * r2**2 * (t - math.sin(t))
    a2 = 0.5 * r1**2 * (p - math.sin(p))
    answer = a1+a2

answer = float(round(1000 * answer)) / 1000
print('%.3f' % answer)
