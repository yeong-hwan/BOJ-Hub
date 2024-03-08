xs, ys = [], []

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xs.append(xs[0])
ys.append(ys[0])

x_sum, y_sum = 0, 0

for idx in range(N):
    x_sum += xs[idx] * ys[idx+1]
    y_sum += ys[idx] * xs[idx+1]

area = abs((x_sum - y_sum) / 2)
print(round(area, 1))
