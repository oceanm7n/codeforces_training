line = input().split()

for i in range(len(line)):
    line[i] = int(line[i])

combos = []
for i in range(4):
    current = line[:i]
    current.extend(line[i + 1:])
    combos.append(current)

flag = 0
for i in combos:
    i.sort()
    if abs(i[0] - i[1]) < i[2] < i[0] + i[1]:
        flag = 1
        break
    elif abs(i[0] - i[1]) < i[2] <= i[0] + i[1]:
        flag = 2

if flag == 1:
    print("TRIANGLE")
elif flag == 2:
    print("SEGMENT")
else: print('IMPOSSIBLE')