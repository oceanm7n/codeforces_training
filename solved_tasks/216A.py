a, b, c = map(int, input().split())

answer = a*b*c - (a - 1) * (b - 1) * (c - 1)
print(answer)