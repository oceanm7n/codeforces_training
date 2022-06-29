stones = {'Power': 'purple', 'Time':'green', 'Space':'blue', 'Soul':'orange','Reality':'red', 'Mind':'yellow'}
stones_list = {'purple','green', 'blue', 'orange', 'red', 'yellow'}
st = []

n = int(input())
for i in range(n):
    st.append(input())
sto = set(st)
diff = stones_list.difference(sto)
diff = list(diff)
print(len(diff))
for d in diff:
    keys = [k for k, v in stones.items() if v == d]
    print(*keys)

