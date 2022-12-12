# read input file
with open("input-07.txt") as f:
    data = f.read().split("$ ")

# generate tree
tree = {}
current_path = ""
for line in data[2:]:
    lines = line.splitlines()
    cmd = lines[0].split(" ")[0]
    print(current_path)
    if cmd == "cd":
        folder = lines[0].split(" ")[1]
        if folder == "..":
            current_path = current_path[: current_path.rfind("/")]
        elif folder == "/":
            current_path = ""
        else:
            current_path += ("/" if folder != "/" else "") + folder
    elif cmd == "ls":
        files = lines[1:]
        if current_path in tree:
            print("shit")
        tree.setdefault(current_path, 0)
        for file in files:
            size, name = file.split(" ")
            if size == "dir":
                continue
            tree[current_path] += int(size)

tree_sums = {}
for key, value in tree.items():
    current_path = ""
    for t in key.split("/"):
        current_path += ("/" if current_path != "" else "") + t
        tree_sums.setdefault(current_path, 0)
        tree_sums[current_path] += value

sum([x for x in tree_sums.values() if x < 100000])

missing = 30000000 - (70000000 - tree_sums[""])
current_delta = 10**12
for key, value in tree_sums.items():

    if value >= missing:
        if value - missing < current_delta:
            current_delta = value - missing
            current_key = key
            print(key, value, value - missing)


from pprint import pprint

pprint(tree_sums)
