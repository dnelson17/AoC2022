
# %%
import json

def read_input(file_name: str) -> str:
    with open(file_name) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


ex = read_input("example7.txt")

ex = read_input("input7.txt")


# %%
dir_dict = {"/":{}}
cur_dir_l = []
cur_d = dir_dict
# print(dir_dict)
for line in ex:
    print(line)
    if line.startswith("$ "):
        line = line[2:]
        if line == "ls":
            continue
        if line.startswith("cd "):
            new_dir = line[3:]
            if new_dir == "..":
                cur_dir_l.pop()
            else:
                cur_dir_l.append(new_dir)
            cur_d = dir_dict
            for dir_name in cur_dir_l:
                cur_d = cur_d[dir_name]
    elif line.startswith("dir"):
        new_dir_name = line[4:]
        cur_d[new_dir_name] = {}
    else:
        [file_size,file_name] = line.split(" ")
        cur_d[file_name] = int(file_size)
    
    print(json.dumps(dir_dict, sort_keys=True, indent=4), sep="\n")
    print("cur_dir_l:", cur_dir_l)
    print("cur_d", json.dumps(cur_d, sort_keys=True, indent=4), sep="\n")
    print("\n")


# %%
print(json.dumps(dir_dict, sort_keys=True, indent=4))


# %%
# def get_totals(dir_dict):
#     new_dict = {}
#     total = 0
#     for key, value in dir_dict.items():
#         if isinstance(value, dict):
#             new_dict[key] = get_totals(value)
#         else:
#             total += value
#             new_dict[key] = value
#     new_dict["total"] = total
#     return new_dict


def get_totals(d: dict) -> dict:
    new_dict = {}
    total = 0
    for key, value in d.items():
        if isinstance(value, dict):
            new_dict[key] = get_totals(value)
            total += new_dict[key]["total"]
        else:
            total += value
    new_dict["total"] = total
    return new_dict

totals_dict = get_totals(dir_dict.copy())

# %%
print(json.dumps(totals_dict["/"], sort_keys=True, indent=4))


# %%
def get_total_under_max(d: dict, max_size: int = 100_000) -> int:
    total = 0
    # for value in d.values():
    for key, value in d.items():
        if isinstance(value, dict):
            value = get_total_under_max(value)
        
        print(value, max_size, value < max_size)
        if value < max_size:
            print("fits")
            total += value
        else:
            print("too big")
        print(key,value)
        
    return total

get_total_under_max(totals_dict)


# %%
import pandas as pd

df = pd.json_normalize(totals_dict["/"], sep='_')
df.columns = [col.replace("total","/").replace("_total","").replace("_/","") for col in df.columns]
df

# %%
totals = df.loc[0]
totals

# %% part 1
totals[totals < 100_000].sum()

# %%
total_used_space = totals.max()
print(f"{total_used_space:_}")

# %%
total_space = 70_000_000
max_allowed_files = 40_000_000
amount_needed_to_clear = total_used_space - max_allowed_files

# %%
totals[totals > amount_needed_to_clear].sort_values().min()


# %%


