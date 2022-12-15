# read input-15.txt
with open("input-15.txt") as f:
    data = f.read().splitlines()

# parse lines for the like
# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
line_to_check = 2000000
occupied_on_line = set()
beacons_on_line = set()

max_coord = 4000_000
min_coord = 0
occupied = dict()

for line in data:
    print(line)
    line = line.split(" ")
    x = int(line[2].split("=")[1][:-1])
    y = int(line[3].split("=")[1][:-1])
    bx = int(line[8].split("=")[1][:-1])
    by = int(line[9].split("=")[1])

    # manhattan distance between x,y and bx,by
    distance = abs(x - bx) + abs(y - by)

    # find position on line y=10 which are within distance from x,y
    vertical_distance = abs(y - line_to_check)
    if vertical_distance <= distance:
        # find x positions
        for i in range(
            x - (distance - vertical_distance), x + (distance - vertical_distance) + 1
        ):
            occupied_on_line.add(i)
    if by == line_to_check:
        beacons_on_line.add(bx)

    for ty in range(y - distance, y + distance):

        _ = occupied.setdefault(ty, set())

        new_coords = (x - (distance - abs(y - ty)), x + (distance - abs(y - ty)))
        # check if within max min coords
        if new_coords[0] <= max_coord or new_coords[1] >= min_coord:
            occupied[ty].add(new_coords)

    # find occupied positions

len(occupied_on_line.difference(beacons_on_line))

ll = list(occupied[11])
ll.sort(key=lambda x: x[0])


def reduce_overlap(sorted_list, current_segment=None):

    if len(sorted_list) == 0:
        return current_segment

    if current_segment is None:
        current_segment = sorted_list[0]
        return reduce_overlap(sorted_list[1:], current_segment)

    line = sorted_list[0]
    if line[0] <= current_segment[1] + 1:
        current_segment = (current_segment[0], max(current_segment[1], line[1]))
        return reduce_overlap(sorted_list[1:], current_segment)
    else:
        return current_segment, reduce_overlap(sorted_list[1:])


for k, v in occupied.items():
    if k < min_coord or k > max_coord:
        continue
    ll = list(v)
    ll.sort(key=lambda x: x[0])
    overlap = reduce_overlap(ll)
    if isinstance(overlap[0], tuple):
        print(k, ll)
        print(overlap)

        y = k
        x = overlap[0][1] + 1
        break

print(x * max_coord + y)
