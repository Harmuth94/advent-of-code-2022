import networkx

G = networkx.DiGraph()

# get txt maze from input-12.txt
with open("input-12.txt") as f:
    txt_maze = f.read()

maze = [list(x) for x in txt_maze.split('\n')]

# get index of value 'S' and 'E'

for i, row in enumerate(maze):
    for j, col in enumerate(row):
        G.add_node((i, j), height=ord(col.replace('S','a').replace('E','z')))
        if col == 'S':
            start = (i, j)
            print(i, j)
        elif col == 'E':
            end = (i, j)
            print(i, j)
for i, row in enumerate(maze):
    for j, col in enumerate(row):
        # if height difference is less than 2, add edge
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # check if node exists
            if (i+direction[0], j+direction[1]) in G.nodes:
                if G.nodes[(i, j)]['height'] - G.nodes[(i+direction[0], j+direction[1])]['height'] > -2:
                    print("adding edge", (i, j), (i+direction[0], j+direction[1]))
                    G.add_edge((i, j), (i+direction[0], j+direction[1]))

print(networkx.shortest_path_length(G, start, end))

# visual inspection of maze
# we need to start in the first column which is adjacent to the b

min_dist = 10**12
for i in range(len(maze)):
    start = (i, 0)
    end = end
    dist = networkx.shortest_path_length(G, start, end)
    if dist < min_dist:
        min_dist = dist
        min_start = start

print(min_dist, min_start)