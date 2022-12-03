# %%
alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
value_dict = dict(zip(list(alphabet_str) + list(alphabet_str.upper()),range(1,53)))
value_dict

def get_overlap_sum(file_name):
    total = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            split = len(line)//2
            left = set(line[:split])
            right = set(line[split:])
            overlap = left & right
            total += value_dict[next(iter(overlap))]
    return total
    

# %%
get_overlap_sum("example3.txt")


# %%
get_overlap_sum("input3.txt")


# %%
def get_group_overlap_sum(file_name):
    total = 0
    with open(file_name, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line1,line2,line3 in zip(lines[::3],lines[1::3],lines[2::3]):
            overlap = set(line1) & set(line2) & set(line3)
            total += value_dict[next(iter(overlap))]
    return total


# %%
get_group_overlap_sum("example3.txt")


# %%
get_group_overlap_sum("input3.txt")


# %%
