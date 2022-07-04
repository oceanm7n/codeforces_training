for i in range(int(input())):
    a = int(input())
    if a % 2 != 0:
        print('-1')
    else:
        print(f'0 0 {a//2}')