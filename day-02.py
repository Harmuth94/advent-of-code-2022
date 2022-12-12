# load input-02.txt data
with open("input-02.txt") as f:
    data = f.read().splitlines()

# part 1
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# X beats C, Y beats A, and Z beats B
# X draws with A, Y draws with B, and Z draws with C
# 6 points for X,Y,Z win, 3 points for draw, 0 points for loss
# Win with Z is 3 points, Paper is 2 points, and Rock is 1 point

xyz_point_map = {
    "X": {"C": 6, "A": 3, "B": 0},
    "Y": {"A": 6, "B": 3, "C": 0},
    "Z": {"B": 6, "C": 3, "A": 0},
}

bonus_map = {"X": 1, "Y": 2, "Z": 3}

score = 0
for line in data:
    abc = line[0]
    xyz = line[2]

    round_score = xyz_point_map[xyz][abc]
    score += round_score + bonus_map[xyz]


print(score)

# part 2
# X for Losing, Y for Drawing, and Z for Winning
abc_to_xyz_map = {
    "A": {"X": "Z", "Y": "X", "Z": "Y"},
    "B": {"X": "X", "Y": "Y", "Z": "Z"},
    "C": {"X": "Y", "Y": "Z", "Z": "X"},
}

score = 0
for line in data:
    abc = line[0]
    outcome = line[2]
    xyz = abc_to_xyz_map[abc][outcome]
    round_score = xyz_point_map[xyz][abc]
    score += round_score + bonus_map[xyz]

print(score)
