def read_input():
    n = int(input())
    d = [int(i) for i in input().split(" ")]
    a, b = [int(i) for i in input().split(" ")]
    return n, d, a, b


def solve(n, d, a, b):
    years = 0
    for i in range(a, b):
        years += d[i-1]
    return years

def main():
    n, d, a, b = read_input()
    answer = solve(n, d, a, b)
    print(answer)



if __name__ == "__main__":
    main()