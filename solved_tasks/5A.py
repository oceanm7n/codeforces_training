from sys import stdin
members = []

result = 0
while True:
    st = stdin.readline().strip()
    if len(st) < 1: 
        break
    if st[0] == '+':
        members.append(st[1:])
    
    elif st[0] == '-':
        members.remove(st[1:])
    
    else:
        result += len(st[st.index(':') + 1:])*len(members)
        
print(result)