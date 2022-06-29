def read_input():
    n = int(input())
    l = [int(i) for i in input().split(" ")]
    return n, l


def solve(n, l):
    res = {}
    for i in l:
        if i in res.keys():
            res[i] += 1
        else:
            res[i] = 1
    return (max(res.values()), len(res.keys()))


def main():
    n, l = read_input()
    answer = solve(n, l)
    print(answer[0], answer[1])



if __name__ == "__main__":
    main()