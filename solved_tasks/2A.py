game = {}
n = int(input())

for i in range(n):
    st = input().split()
    if st[0] not in game.keys():
        game[st[0]] = [int(st[1]), i]
    
    else:
        game[st[0]] = [game[st[0]][0] + int(st[1]), i]
    
    print(game)

maximum = 0
winners = []
min = n

for i in game:
    if game[i][0] > maximum:
        maximum = game[i][0]

for i in game:
    if game[i][0] == maximum:
        winners.append(i)

for i in winners:
    if game[i][1] < min and game[i][1] > 0:
        min = game[i][1]
        winner = i

print(winners)
# print(game)