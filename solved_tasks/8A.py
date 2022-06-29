line = input()
a = input()
b = input()

result = ''
if a in line and b in line:
    if a == b:
        result = 'both'
    elif line.count(b) == 1:
        if line.index(a) < line.index(b):
            result = 'forward'
        elif line.index(a) > line.index(b):
            result = 'backward'
    elif line.count(b) > 1:
        if line.index(a) < line.index(b) < line[line.index(b):].index(a):
            result = 'both' 
        elif line[-len(b):] == b:
            result = 'forward'
        


if result:
    print(result)
else: 
    print('fantasy')