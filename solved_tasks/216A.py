a, b, c = map(int, input().split())
diag = c - 1
left = a + b - 1
right = a * b
s = left * diag + right
# print(diag)
# print(left)
# print(right)
print(s)
