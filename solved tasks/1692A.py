def read_input():
    n = int(input())
    data = []
    for i in range(n):
        a, b, c, d = input().split(" ")
        data.append([int(a), int(b), int(c), int(d)])
    return n, data
            
        

def main():
    
    answer = []
    t, data = read_input()
    
    for values in data:
        cnt = 0
        max = values[0]
        for i in (1, 2, 3):
            if values[i] > max:
                cnt +=1
        answer.append(cnt)

    
    for a in answer:
        print(a)



if __name__ == "__main__":
    main()