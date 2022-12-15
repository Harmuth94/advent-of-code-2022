# read input-14.txt
with open("input-14.txt") as f:
    txt_input = f.read().splitlines()

import numpy as np

# get max value of x and y
max_x = 0
max_y = 0
min_x = 10000
min_y = 0
for line in txt_input:
    coords = line.split('->')
    for coord in coords:
        x, y = coord.split(',')
        if int(x) > max_x:
            max_x = int(x)
        if int(y) > max_y:
            max_y = int(y)
        if int(x) < min_x:
            min_x = int(x)
# draw the maze
maze = np.full((max_y+1, max_x+1), '.')

for line in txt_input:
    _from = None
    coords = line.split('->')
    for coord in coords:
        x, y = coord.split(',')
        _to = (int(x), int(y))
        if _from is not None:
            # set everythin in between from and to to #
            print(_from, _to)
            maze[min(_from[1], _to[1]):max(_from[1], _to[1])+1, min(_from[0], _to[0]):max(_from[0], _to[0])+1] = '#'
        _from = _to

def drop(x, y, maze):
    # if below is empty, drop
    if maze[y+1, x] == '.':
        return drop(x, y+1, maze)
    # if below is wall, and left or right is empty
    elif maze[y+1, x-1] == '.':
        
        return drop(x-1, y+1, maze)
    elif maze[y+1, x+1] == '.': 
        
        return drop(x+1, y+1, maze)
    else:
        
        return x,y

for i in range(100000):
    try:
        x, y = drop(500, 0, maze)
    except IndexError:
        break
    maze[y, x] = 'o'

    for row in maze:
        print(''.join(row[min_x:]))
print(i)

# draw the maze
maze = np.full((max_y+1+2, 1000), '.')

for line in txt_input:
    _from = None
    coords = line.split('->')
    for coord in coords:
        x, y = coord.split(',')
        _to = (int(x), int(y))
        if _from is not None:
            # set everythin in between from and to to #
            print(_from, _to)
            maze[min(_from[1], _to[1]):max(_from[1], _to[1])+1, min(_from[0], _to[0]):max(_from[0], _to[0])+1] = '#'
        _from = _to

maze[max_y + 2,:] = '#'

for i in range(100000):
    if maze[0, 500] == 'o':
        print(i)
        break
    x, y = drop(500, 0, maze)
    maze[y, x] = 'o'


for row in maze:
        print(''.join(row))
print(i+1)