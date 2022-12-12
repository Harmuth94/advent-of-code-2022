# read input 3
with open("input-03.txt") as f:
    data = f.read().splitlines()


def get_overlap(rucksack):
    # split rucksack into 2 parts. Equal size

    # get the first part
    rucksack_1 = set(rucksack[: len(rucksack) // 2])
    # get the second part
    rucksack_2 = set(rucksack[len(rucksack) // 2 :])

    overlap = rucksack_1.intersection(rucksack_2)

    return overlap


def priority(item):
    # a = 1, z = 26
    # A = 27, Z = 52

    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


total_prio_sum = 0
for rucksack in data:
    overlap = get_overlap(rucksack)
    assert len(overlap) == 1
    item = overlap.pop()
    prio = priority(item)
    print(rucksack, item, prio)
    total_prio_sum += prio

print(total_prio_sum)


# part 2
total_prio_sum = 0
# group rucksacks in 3s
rucksacks = []
for i in range(0, len(data), 3):
    rucksacks.append(data[i : i + 3])

for group in rucksacks:
    overlap = set(group[0])
    overlap = overlap.intersection((group[1]))
    overlap = overlap.intersection((group[2]))
    assert len(overlap) == 1
    item = overlap.pop()
    prio = priority(item)
    print(group, item, prio)
    total_prio_sum += prio

print(total_prio_sum)
