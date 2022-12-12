# read first 9 lines and transpose
with open("input-05.txt") as f:
    data = f.read().splitlines()

# part 1
crates = {i: [] for i in range(1, 10)}
for line in data[:8][::-1]:
    for i in range(1, 10):
        if line[1 + (i - 1) * 4] != " ":
            print(1 + (i - 1) * 4)
            crates[i].append(line[1 + (i - 1) * 4])

for line in data[10:]:
    _, n, _, _from, _, _to = line.split(" ")

    for _ in range(int(n)):
        crates[int(_to)].append(crates[int(_from)].pop())

print("".join([x[-1] for x in crates.values()]))

# part 2
# part 1
crates = {i: [] for i in range(1, 10)}
for line in data[:8][::-1]:
    for i in range(1, 10):
        if line[1 + (i - 1) * 4] != " ":
            print(1 + (i - 1) * 4)
            crates[i].append(line[1 + (i - 1) * 4])

for line in data[10:]:
    _, n, _, _from, _, _to = line.split(" ")
    to_move = crates[int(_from)][-int(n) :]
    for _ in range(int(n)):
        crates[int(_from)].pop()

    crates[int(_to)].extend(to_move)

print("".join([x[-1] for x in crates.values()]))
