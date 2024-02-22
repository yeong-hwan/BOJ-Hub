S = input()
result = ""

temp = ""
reverse_toggle = True

for letter in S:
    if letter == " ":
        temp = temp[::-1]
        result += temp
        temp = ""

        result += letter
    elif letter == "<":
        temp = temp[::-1]
        result += temp
        temp = ""

        reverse_toggle = False
        result += letter
    elif letter == ">":
        reverse_toggle = True
        result += letter
    
    elif reverse_toggle:
        temp += letter
    else:
        result += letter

temp = temp[::-1]
result += temp
temp = ""

print(result)