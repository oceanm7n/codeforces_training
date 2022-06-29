def solve():
    n = int(input())
    
    game = []
    leaderboards = {}

    for i in range(n):
        name, score = input().split(" ")
        score = int(score)
        game.append([name, score])

    max = 0
    for i in game:
        [name, score] = i
        if name not in leaderboards.keys():
            leaderboards[name] = score
        else:
            leaderboards[name] += score
        
        if leaderboards[name] > max:
            max = leaderboards[name]

    
    winners = []
    max = 0
    for p in leaderboards.keys():
        if leaderboards[p] > max:
            max = leaderboards[p]
            winners = [p]
        elif leaderboards[p] == max:
            winners.append(p)
    

    if len(winners) == 1:
        print(winners[0])
        return
    
    second_leaderboards = {}


    for i in game:
        [name, score] = i
        if name in winners:
            if name not in second_leaderboards.keys():
                second_leaderboards[name] = score
            else:
                second_leaderboards[name] += score
            if second_leaderboards[name] >= max:
                print(name)
                return


solve()