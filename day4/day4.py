# %%
def get_full_overlaps(file_name):
    total = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            left, right = line.strip().split(",")
            l_start, l_stop = left.split("-")
            r_start, r_stop = right.split("-")
            l_range = set(range(int(l_start),int(l_stop)+1))
            r_range = set(range(int(r_start),int(r_stop)+1))
            if l_range == r_range:
                total += 1
            else:
                total += l_range.issubset(r_range) + r_range.issubset(l_range)
    return total

# %%
get_full_overlaps("example4.txt")

# %%
get_full_overlaps("input4.txt")


# %%
def get_part_overlaps(file_name):
    total = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            left, right = line.strip().split(",")
            l_start, l_stop = left.split("-")
            r_start, r_stop = right.split("-")
            l_range = set(range(int(l_start),int(l_stop)+1))
            r_range = set(range(int(r_start),int(r_stop)+1))
            total += len(l_range & r_range) > 0
    return total

# %%
get_part_overlaps("example4.txt")

# %%
get_part_overlaps("input4.txt")

