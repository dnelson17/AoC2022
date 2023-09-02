
# %%
import numpy as np

def read_input(file_name: str) -> str:
    with open(file_name) as f:
        lines = np.array([list(line.strip()) for line in f.readlines()]).astype(int)
    return lines


# %%
ex = read_input("example8.txt")
ex = read_input("input8.txt")
ex

# %%
import pandas as pd

pd.DataFrame(ex).style.background_gradient()


# %%
res = np.zeros_like(ex)
res[0] = 1
res[-1] = 1
res[:,0] = 1
res[:,-1] = 1
for ((i,j), val) in np.ndenumerate(ex):
    if i==0 or j==0 or i==ex.shape[0]-1 or j==ex.shape[1]-1:
        print(f"({i},{j}) edge")
        continue
    # checking if it is visible from the top
    elif ex[i,j] > ex[:i,j].max():
        res[i,j] = 1
        print(f"({i},{j}) {val} visible from the left")
        continue
    # checking if it is visible from the right
    elif ex[i,j] > ex[i,j+1:].max():
        res[i,j] = 1
        print(f"({i},{j}) {val} visible from the right")
        continue
    # checking if it is visible from the bottom
    elif ex[i,j] > ex[i+1:,j].max():
        res[i,j] = 1
        print(f"({i},{j}) {val} visible from the bottom")
        continue
    # checking if it is visible from the left
    elif ex[i,j] > ex[i,:j].max():
        res[i,j] = 1
        print(f"({i},{j}) {val} visible from the left")
        continue
    else:
        print(f"({i},{j}) {val} not visible")

print(res)
res.sum()

# %%
# might be a fun exercise to write something that will graph all of the tiles
# in like a heat map kind of thing
# and tell you where they are visible from so like an arrow udlr on each tile 
# saying it was visible from all of these angles

# a 3 plot could be cool too
# could put in some nice wee tree renders



# %% PART 2
a = np.zeros((4,5,5))
a[0][0][0] = 1
a.sum(axis=0)


# %%
# (i,j) = (1,2)
(i,j) = (2,3)

val = ex[i,j]
print(ex,"\n")
print((i,j), val, "\n")
# print("u",ex[:i,j][::-1],np.where(ex[:i,j][::-1] >= val)[0]+1)
# print("l",ex[i,:j][::-1],np.where(ex[i,:j][::-1] >= val)[0]+1)
# print("r",ex[i,j+1:],np.where(ex[i,j+1:] >= val)[0]+1)
# print("d",ex[i+1:,j],np.where(ex[i+1:,j] >= val)[0]+1)

u = ex[:i,j][::-1]
l = ex[i,:j][::-1]
r = ex[i+1:,j]
d = ex[i,j+1:]

def get_view_dist(arr: np.array, val: int) -> int:
    blocking_trees = np.where(arr >= val)[0]
    if len(blocking_trees) == 0:
        return len(arr)
    else:
        return blocking_trees.min()+1



# get_view_dist = lambda arr, val: np.where(arr >= val)[0].max()+1
print("u",get_view_dist(u,val),u)
print("l",get_view_dist(l,val),l)
print("r",get_view_dist(r,val),r)
print("d",get_view_dist(d,val),d)



# %%
p2_res = np.zeros((4,*(ex.shape)))
for ((i,j), val) in np.ndenumerate(ex):
    if i==0 or j==0 or i==ex.shape[0]-1 or j==ex.shape[1]-1:
        continue
    
    u = ex[:i,j][::-1]
    l = ex[i,:j][::-1]
    r = ex[i+1:,j]
    d = ex[i,j+1:]
    
    p2_res[0,i,j] = get_view_dist(u,val)
    p2_res[1,i,j] = get_view_dist(l,val)
    p2_res[2,i,j] = get_view_dist(r,val)
    p2_res[3,i,j] = get_view_dist(d,val)

print(p2_res)

# %%
scenic_scores = p2_res.prod(axis=0)
print(scenic_scores)

# %%
int(scenic_scores.max())

# %%
