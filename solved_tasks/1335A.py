tests = int(input())

for i in range(tests):
    count_of_tests = int(input())
    if count_of_tests == 1 or count_of_tests == 2:
        print('0')
    else:
        d = ((count_of_tests-1) // 2)
        print(d)