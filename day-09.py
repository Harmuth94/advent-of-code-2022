# read input file
with open("input-09.txt") as f:
    data = f.read().splitlines()

import numpy as np



seen_positions = {(0,0)}
head_current_position = np.array([0,0])
tail_current_position = np.array([0,0])
tail_current_position-head_current_position


for line in data:
    direction, distance = line.split(' ')

    for _ in range(int(distance)):
        if direction == 'U':
            head_current_position += np.array([0,1])
        elif direction == 'D':
            head_current_position += np.array([0,-1])
        elif direction == 'L':
            head_current_position += np.array([-1,0])
        elif direction == 'R':
            head_current_position += np.array([1,0])
        else:
            print("Unknown direction: {}".format(direction))
            exit(1)
        #seen_positions.add(tuple(head_current_position))
        
        head_tail_distance = head_current_position-tail_current_position
        while True:
            if max(abs(head_tail_distance)) > 1:
                if head_tail_distance[0] == 0: # move vertically
                    tail_current_position += np.array([0,np.sign(head_tail_distance[1])])
                elif head_tail_distance[1] == 0: # move horizontally
                    tail_current_position += np.array([np.sign(head_tail_distance[0]),0])
                else: # move diagonally
                    tail_current_position += np.array([np.sign(head_tail_distance[0]),np.sign(head_tail_distance[1])])
                
                seen_positions.add(tuple(tail_current_position))
                head_tail_distance = head_current_position-tail_current_position
                
            else:
                break

len(seen_positions)
## part 2



seen_positions = {(0,0)}
current_positions = [np.array([0,0]) for _ in range(10)]


for line in data:
    direction, distance = line.split(' ')

    for _ in range(int(distance)):
        if direction == 'U':
            current_positions[0] += np.array([0,1])
        elif direction == 'D':
            current_positions[0] += np.array([0,-1])
        elif direction == 'L':
            current_positions[0] += np.array([-1,0])
        elif direction == 'R':
            current_positions[0] += np.array([1,0])
        else:
            print("Unknown direction: {}".format(direction))
            exit(1)
        
        for rope in range(1,10):
            
            head_tail_distance = current_positions[rope-1]-current_positions[rope]
            while True:
                if max(abs(head_tail_distance)) > 1:
                    if head_tail_distance[0] == 0: # move vertically
                        current_positions[rope] += np.array([0,np.sign(head_tail_distance[1])])
                    elif head_tail_distance[1] == 0: # move horizontally
                        current_positions[rope] += np.array([np.sign(head_tail_distance[0]),0])
                    else: # move diagonally'
                        current_positions[rope] += np.array([np.sign(head_tail_distance[0]),np.sign(head_tail_distance[1])])
                    
                    
                    head_tail_distance = current_positions[rope-1]-current_positions[rope]
                    if rope == 9:
                        seen_positions.add(tuple(current_positions[rope]))
                else:
                    break

len(seen_positions)