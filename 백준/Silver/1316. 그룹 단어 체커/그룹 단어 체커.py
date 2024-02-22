count = int(input())
group_word = 0

for _ in range(count):
    word = input()
    wrong_count = 0
    for i in range(97, 123):
        letter_list = []
        letter = chr(i)

        for j in range(len(word)):
            if word[j] == letter:
                letter_list.append(j)

    
        for k in range(len(letter_list)-1):
            if letter_list[k] != letter_list[k+1] - 1:
                wrong_count += 1

    if wrong_count == 0:
        group_word += 1

print(group_word)