n = input() # a1

# 수평 수직
move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]
nx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = int(n[1]) 


result = 0
for i in range(len(nx)):
    if n[0] == nx[i]:
        x = i + 1
        break
for i in move:
    if 0 < x + i[0] < 8 and 0 < y + i[1] < 8:
        result += 1

print(result)