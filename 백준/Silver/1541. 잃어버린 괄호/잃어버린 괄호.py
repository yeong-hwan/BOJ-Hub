equations = input().split("-")

result = 0

numbers = equations.pop(0).split("+")
for number in numbers:
    result += int(number)


for equation in equations:
    numbers = equation.split("+")
    for number in numbers:
        result -= int(number)

print(result)