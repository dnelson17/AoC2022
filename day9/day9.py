
# %%
from math import hypot

def read_input(file_name: str) -> list:
    with open(file_name) as f:
        lines = [line.strip().split(" ") for line in f.readlines()]
        lines = [(char,int(num)) for char,num in lines]
    return lines

# %%
ex = read_input("example9.txt")
ex = read_input("input9.txt")

# %%
ex


# %%
head_pos_l = [(0,0)]
tail_pos_l = [(0,0)]

for direction, steps in ex:
    for _ in range(steps):
        head_x, head_y = head_pos_l[-1]
        if direction == "U":
            head_x, head_y = head_x + 1, head_y
        elif direction == "D":
            head_x, head_y = head_x - 1, head_y
        elif direction == "L":
            head_x, head_y = head_x, head_y - 1
        elif direction == "R":
            head_x, head_y = head_x, head_y + 1
        head_pos_l.append((head_x, head_y))
        
        tail_x, tail_y = tail_pos_l[-1]
        x_diff = head_x - tail_x
        y_diff = head_y - tail_y
        
        if hypot(x_diff,y_diff) > hypot(1,1):
            tail_x += np.sign(x_diff)
            tail_y += np.sign(y_diff)
        elif abs(x_diff) > 1:
            tail_x += np.sign(x_diff)
        elif abs(y_diff) > 1:
            tail_y += np.sign(y_diff)
        
        tail_pos_l.append((tail_x,tail_y))
        
        
    
head_pos_l

# %%
import pandas as pd
import numpy as np

max_locs = pd.DataFrame(head_pos_l,columns=["x","y"]).max()
x_max = max_locs.loc["x"]
y_max = max_locs.loc["y"]


# %%
a = np.zeros((3,3))
np.array_str(a)

print_arr = ["".join(item) for item in a.astype(int).astype(str)]
print(*print_arr, sep="\n")

# %%
for ((head_x,head_y),(tail_x,tail_y)) in zip(head_pos_l,tail_pos_l):
    print("")
    arr = np.full((x_max+1, y_max+1), '.')
    arr[0,0] = "s"
    arr[tail_x,tail_y] = "T"
    arr[head_x,head_y] = "H"
    print_arr = ["".join(item) for item in arr[::-1].astype(str)]
    print(*print_arr, "", sep="\n")


# %%
len(set(tail_pos_l))


# %%



