while True:
    string = input()

    if string == ".":
        break
    
    if string[-1] != ".":
        print("no")
        continue

    parenthesis_cnt, bracket_cnt = 0, 0
    string = list(string)[::-1]

    recent = []

    while string:
        letter = string.pop()
        if letter == "(":
            parenthesis_cnt += 1
            recent.append("parenthesis")
        elif letter == ")":
            parenthesis_cnt -= 1
            if len(recent) == 0:
                break
            if recent.pop() != "parenthesis":
                break
        elif letter == "[":
            bracket_cnt += 1
            recent.append("bracket")
        elif letter == "]":
            bracket_cnt -= 1
            if len(recent) == 0:
                break
            if recent.pop() != "bracket":
                break

        if parenthesis_cnt < 0 or bracket_cnt < 0:
            break
    
    if parenthesis_cnt != 0 or bracket_cnt != 0:
        print("no")
    else:
        print("yes")

