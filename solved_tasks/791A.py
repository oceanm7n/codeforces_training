a, b = map(int, input().split())
count = 0
flag = True
while flag:
    a = a * 3
    b = b * 2
    count += 1
    if a > b:
        flag = False
print(count)
