# %%

# A / X -> rock -> 1
# B / Y -> paper -> 2
# C / Z -> scissors -> 3

shape_points = {"X":1, "Y":2, "Z":3}

outcome_points = {
    ("A","X"): 3,
    ("A","Y"): 6,
    ("A","Z"): 0,
    ("B","X"): 0,
    ("B","Y"): 3,
    ("B","Z"): 6,
    ("C","X"): 6,
    ("C","Y"): 0,
    ("C","Z"): 3
}

def read_lines(file_name):
    with open(file_name, "r") as f:
        lines = [line.strip().split(" ") for line in f.readlines()]
    return lines


def get_scores_p1(rounds):
    score = 0
    for [opp, you] in rounds:
        score += shape_points[you] + outcome_points[(opp, you)]
    return score


# %% Part 1 - Example
get_scores_p1(read_lines("example2.txt"))

# %% Part 1
get_scores_p1(read_lines("input2.txt"))

# %%
# X lose
# Y draw
# Z win

p2_outcome_points = {
    ("A","X"): 0 + 3,
    ("A","Y"): 3 + 1,
    ("A","Z"): 6 + 2,
    ("B","X"): 0 + 1,
    ("B","Y"): 3 + 2,
    ("B","Z"): 6 + 3,
    ("C","X"): 0 + 2,
    ("C","Y"): 3 + 3,
    ("C","Z"): 6 + 1
}


def get_scores_p2(rounds):
    score = 0
    for [opp, you] in rounds:
        score += p2_outcome_points[(opp, you)]
    return score

# %% Part 1 - Example
get_scores_p2(read_lines("example2.txt"))

# %% Part 1
get_scores_p2(read_lines("input2.txt"))



