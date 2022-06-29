file = open('input.txt', 'r')
temp = []
for i in file:
    temp.append(i)
file.close()
door, hand = temp[0][:-1], int(temp[1])

if door == 'front':
    if hand == 1:
        res = 'L'
    else:
        res = 'R'

else:
    if hand == 1:
        res = 'R'
    else:
        res = 'L'

file = open('output.txt', 'w')
file.write(res)
file.close()