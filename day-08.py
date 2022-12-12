# read input file
with open("input-08.txt") as f:
    data = f.read().splitlines()

data = [[int(x) for x in line] for line in data]

import numpy as np

# convert to numpy array
np_array = np.array(data)
match_counter = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        match = False
        value = np_array[i,j]
        # check above
        if i > 0:
            if np_array[:i,j].max() < value:
                print("found match above")
                match = True
        else:
            match = True
        # check below
        if i < 98:
            if np_array[i+1:,j].max() < value:
                print("found match below")
                match = True
        else:
            match = True

        # check left
        if j > 0:
            if np_array[i,:j].max() < value:
                print("found match left")
                match = True
        else:
            match = True

        # check right
        if j < 98:
            if np_array[i,j+1:].max() < value:
                print("found match right")
                match = True
        else:
            match = True

        
        if match:
            match_counter += 1


# convert to numpy array
np_array = np.array(data)
current_max = 0

def get_view_distance(height: int, trees: np.array):
    if trees.max() < height:
        return len(trees)
    return np.argmax(trees >= height) + 1
    

for i in range(len(data)):
    for j in range(len(data[i])):
        if i in (0, 98) or j in (0, 98):
            # on border
            continue
        
        value = np_array[i,j]
        # check above
        # find first value in np_array[:i,j] that is greater than value
        above = get_view_distance(value, np_array[:i,j][::-1])

        # check below
        below = get_view_distance(value, np_array[i+1:,j])

        # check left
        left = get_view_distance(value, np_array[i,:j][::-1])

        # check right
        right = get_view_distance(value, np_array[i,j+1:])

        if above * below * left * right > current_max:
            current_max = above * below * left * right
            print(f"new max: {current_max} at {i}, {j}")
            print(f"above: {above}, below: {below}, left: {left}, right: {right}")
            
        
