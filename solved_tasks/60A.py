n, m = map(int, input().split())
pos = n
move = 1
for i in range(m):
    helps = input().split()
    if helps[2] == 'left':
        pos = min(pos, int(helps[4]) - 1)
    else:
        move = max(move, int(helps[4]) + 1)
if move <= pos:
    print(pos - move + 1)
else:
    print(-1)


