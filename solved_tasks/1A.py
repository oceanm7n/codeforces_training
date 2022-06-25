n, m, a = map(int, input().split())
if n % a != 0:
    n = n // a + 1
else:
    n = n / a
if m % a != 0:
    m = m // a + 1
else:
    m = m / a
print(int(n*m))