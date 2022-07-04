for i in range(int(input())):
    n, m = map(int, input().split())
    case = [[1, 0], [0, 1]]
    answer = [[] for i in range(n)]
    reverse = False
    for y in range(n):
        if (y + 1) % 4 == 0 or (y + 1) % 4 == 1:
            reverse = False
        else:
            reverse = True
        for x in range(int(m / 2)):
            if not reverse:
                answer[y].extend([1, 0])
            else:
                answer[y].extend([0, 1])
            reverse = not reverse
        



    for j in answer:
        print(*j)