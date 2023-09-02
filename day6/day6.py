
# %%
def read_input(file_name: str) -> str:
    with open(file_name) as f:
        line = f.readline()
    return line


def get_first_marker(s: str, win_len: int) -> int:
    it = [s[i:i+win_len] for i in range(len(s)-(win_len-1))]
    return next(i for (i,win) in enumerate(it) if len(set(win)) == win_len) + win_len


# %%
ex = read_input("example6.txt")
get_first_marker(ex,4)


# %% rough work for part 1
print(ex)
it = zip(ex[:-3], ex[1:], ex[2:], ex[3:])
print(*it, sep="\n")


# %%
inp = read_input("input6.txt")
get_first_marker(inp,4)



# %% rough work to generalise 'it' for part 2
print(ex)
win_len = 4
it = [ex[i:i+win_len] for i in range(len(ex)-(win_len-1))]
it


# %%
ex_list = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]

# %%
for s, res in ex_list:
    print(get_first_marker(s,14),res)

# %%
get_first_marker(inp,14)




# %%




# %%



