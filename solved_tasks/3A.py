def dist(start):
    return abs(((end[0] - start[0])**2+(end[1] - start[1])**2)**0.5)


def direction(distences):
    return directions[distences.index(min(distences))]

def move(dir, coords):
    x, y = coords
    if 'U' in dir:
        y += 1
    if 'R' in dir:
        x += 1
    if 'D' in dir:
        y -= 1
    if 'L' in dir:
        x -= 1
    return [x,y]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
directions = ['L', 'LU', 'U', 'RU', 'R', 'RD', 'D', 'LD']
start = list(input())
global end
end = list(input())

start = [letters.index(start[0]), int(start[1]) - 1]
end = [letters.index(end[0]), int(end[1]) - 1]



distance = dist(start)
answer = []
while start != end:
    
    distences = [dist([start[0] - 1, start[1]]), dist([start[0] - 1, start[1] + 1]), dist([start[0], start[1] + 1]), dist([start[0] + 1, start[1] + 1]), dist([start[0] + 1, start[1]]), dist([start[0] + 1, start[1] - 1]), dist([start[0], start[1] - 1]), dist([start[0] - 1, start[1] - 1])]
    dir = direction(distences)
    answer.append(dir)

    start = move(dir, start)
    distance = dist(start)
    # print(start, end)
    # sleep(1)

print(len(answer))
for i in answer:
    print(i)