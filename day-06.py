# read input
with open("input-06.txt") as f:
    data = f.read()

print([len(set(data[i : (i + 4)])) == 4 for i in range(len(data))].index(1) + 4)

print([len(set(data[i : (i + 14)])) == 14 for i in range(len(data))].index(1) + 14)
