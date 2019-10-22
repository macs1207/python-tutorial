f = open("./ch3/input.txt", "r")
ipt_list = []
for ipt in f:
    ipt_list = list(map(int,ipt.strip("\n").split(" ")))
    if ipt_list[0] == 1:
        for idx in range(ipt_list[1]):
            for in_idx in range(ipt_list[1]):
                print("*", end="")
            print()
    elif ipt_list[0] == 2:
        for idx in range(ipt_list[1]):
            for in_idx in range(ipt_list[1] - 1 - idx):
                print(" ", end="")
            for in_idx in range(idx * 2 + 1):
                print("*", end="")
            print()
    elif ipt_list[0] == 3:
        for idx in range(ipt_list[1] // 2 + 1):
            for in_idx in range(ipt_list[1] - 1 - ipt_list[1] // 2 - idx):
                print(" ", end="")
            for in_idx in range(idx * 2 + 1):
                print("*", end="")
            print()
        for idx in range(ipt_list[1], ipt_list[1] // 2 + 1, -1):
            for in_idx in range(ipt_list[1] - idx + 1):
                print(" ", end="")
            for in_idx in range(idx - (ipt_list[1] - idx + 2)):
                print("*", end="")
            print()