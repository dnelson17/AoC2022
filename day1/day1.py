# %%
def read_input(file_name):
    with open(file_name) as f:
        groups = [sum(int(i) for i in line.split("\n")) for line in f.read().strip("\n").split("\n\n")]
    return groups


# %% Testing Example
example_groups = read_input("example1.txt")
print(max(example_groups))

# %% Part 1
groups = read_input("input1.txt")
max(groups)

# %% Part 2
sum(sorted(groups, reverse=True)[:3])
