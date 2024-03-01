N = int(input())

# def count_two(case):
#     two_count = list(case).count('2')
#     return two_count

# result_dicts = [[]]

# for _ in range(30):
#     result_dicts.append([])

# result_dicts[1].append('1')

# for idx in range(2, 7):
#     # print('\nnow:', idx,)
#     # print(result_dicts[idx-1])

#     for prev_case in result_dicts[idx-1]:
#         # print(prev_case)
#         if '1' + prev_case not in result_dicts[idx]:
#             result_dicts[idx].append('1' + prev_case)
        
#         temp = prev_case + '1'
#         if temp not in result_dicts[idx] and temp[::-1] not in result_dicts[idx]:
#             result_dicts[idx].append(prev_case + '1')

#     # even
#     if idx % 2 == 0:
#         result_dicts[idx].append('2' * (idx // 2))


#     print(result_dicts[idx])

# answers = [0]

# for idx in range(1, 31):
#     if idx == 2:
#         answers.append(3)
#         continue

#     temp_result = 0
#     for case in result_dicts[idx]:
#         # only two case
#         if idx == len(case) * 2:
#             twos_len = len(case)
#             temp_result += answers[twos_len]
#             continue

#         two_count = count_two(case)

#         if two_count == 0:
#             temp_result += 1
#         else:
#             temp_result += 2 ** two_count
#     # print(idx, temp_result)
#     answers.append(temp_result)

# print(answers[N])

dp = [1, 1, 3]

for idx in range(3, 31):
    dp.append(dp[idx-2] * 2 + dp[idx-1])

# # exception
# for idx in range(3, 10):
#     # odd
#     if idx // 2 != 0:
#         dp[idx]  = dp[(idx-1) / 2] 
#         dp[id]

#     # even

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    # odd
    if N % 2 != 0:
        print( ( dp[ N ] + dp[ (N-1)//2 ] ) // 2 ) 
    # even
    else:
        print( ( dp[ N ] + dp[ N//2 ] + dp[ N//2 - 1 ] * 2 ) // 2 ) 
