n = int(input())
game = {}
m = 0
for i in range(n):
    name, points = input().split()
    points = int(points)
    if name not in game:
        game[name] = [[points, i+1]]
    else:
        points += game[name][-1][0]
        game[name].append([points, i + 1])

for name in game:
    if game[name][-1][0] > m:
        m = game[name][-1][0]

leaders = []
for name in game:
    if game[name][-1][0] == m:
        leaders.append(name)
winner = []
for name in leaders:
    for points, turn in game[name]:
        if points >= m:
            winner.append([name, turn])
print(sorted(winner, key=lambda x:x[1])[0][0])