coloums = [[] for i in range(8)]
rows = [[] for i in range(8)]

for i in range(8):
    line = input()
    rows[i] = list(line)
    for j in range(8):
        coloums[j].append(line[j])

result = 0

for i in rows:
    if 'W' not in i:
        result += 1

for i in coloums:
    if 'W' not in i:
        result += 1

if result == 16:
    result = 8

print(result)

