# read input-04.txt
with open("input-04.txt") as f:
    data = f.read().splitlines()

# part 1
n_subsets = 0
for pair in data:
    elf1, elf2 = pair.split(",")

    # convert 2-5 to {2,3,4,5}
    elf1 = set(range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1))
    elf2 = set(range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1))

    if elf1.issubset(elf2) or elf2.issubset(elf1):
        print(pair, "YES")
        n_subsets += 1
print(n_subsets)


# part 2
n_intersections = 0
for pair in data:
    elf1, elf2 = pair.split(",")

    elf1 = set(range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1))
    elf2 = set(range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1))

    if elf1.intersection(elf2):
        print(pair, "Intersection")
        n_intersections += 1
print(n_intersections)
