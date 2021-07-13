s = input() # 0110110 

data = []
for i in range(len(s)):
    data.append(int(s[i]))

result = 0
for i in range(len(data)):
    if data[i] > data[i-1]: # 1 
            result += 1

print(result)






# s = input() # 0110110 

# data = []
# for i in range(len(s)):
#     data.append(int(s[i]))

# s_0 = data.count(0)
# s_1 = data.count(1)


# result = 0
# for i in range(len(data)):
#     if s_0 == 0 or s_1 == 0:
#         result = 1
#         break
#     if data[i] > data[i-1]: # 1 
#             result += 1

# print(result)


# for i in range(len(data)):
#     if s_0 > s_1: # 1보다 0이 많다면
#         if data[i] > 1: # 1을 뒤집기
#             count += 1
#             if i == len(data) - 1: 
#                 break
#             elif data[i+1] == '0': # 다음 문자가 0이라면
#                 result += 1
#                 count = 0
#     else: # 0보다 1이 많다면
#         if data[i] == '0': # 0을 뒤집기
#             count += 1
#             if i == len(data) - 1: 
#                 break
#             elif data[i+1] == '1': # 다음 문자가 1이라면
#                 result += 1
#                 count = 0
# if count > 0:
#     result += 1