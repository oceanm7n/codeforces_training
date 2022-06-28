n = int(input())
coords = []
for i in range(n):
    coords.append(input().split())
for i in coords:
    y, x = map(int, i)
    if x == y == 1:
        print(1)
        continue
    resX = 0
    resY = 0
    for j in range(x):
        resX += j + 1
        
    for j in range(1, y):
        resY += x + x*j
    result = resX + resY
    print(result)