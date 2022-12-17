# %%
with open("input5.txt","r") as f:
    crates, commands = f.read().split("\n\n")

command_list = []
for command in commands.split("\n"):
    _,__,command = command.partition("move ")
    move, _, command = command.partition(" from ")
    from_var, ___, to_var = command.partition(" to ")
    command_list.append((int(move), int(from_var), int(to_var)))

crate_list = []
for crate in crates.split("\n"):
    print("|",crate,sep="",end="|\n")
    crate = (crate
             .replace("["," ")
             .replace("]"," ")
             .replace("    ","~")
             .replace("   ","")
             .replace("  ","")
             .replace(" ","")
             .strip()
             )
    crate_list.append(tuple(crate))

crate_list = list(map(list, zip(*crate_list[:-1])))

for i, stack in enumerate(crate_list):
    crate_list[i] = stack[stack.count("~"):][::-1]

crate_list


# %%
for (num_to_move, from_loc, to_loc) in command_list:
    crate_list[to_loc - 1].extend(crate_list[from_loc - 1][-num_to_move:][::-1])
    crate_list[from_loc - 1] = crate_list[from_loc - 1][:-num_to_move]

for crate in crate_list:
    print(crate[-1],end="")


# %%



