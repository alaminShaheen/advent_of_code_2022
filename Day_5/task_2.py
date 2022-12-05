stacks = [[] for _ in range(9)]
lines = []
building_stacks = True
for line in open("input.txt", "r"):
    if building_stacks:
        line = line.rstrip()
        if not line:
            for row_index in range(len(lines) - 2, -1, -1):
                empty = stack_index = 0
                for element in lines[row_index]:
                    if element:
                        empty = 0
                        stacks[stack_index].append(element)
                        stack_index += 1
                    else:
                        empty += 1
                        if empty % 4 == 0:
                            stack_index += 1
            building_stacks = False
            continue
        lines.append(line.split(" "))
    else:
        _, amount, _, from_index, _, to_index = line.strip().split(" ")
        amount, from_index, to_index = int(amount), int(from_index), int(to_index)
        elements = []
        while amount:
            elements.append(stacks[from_index - 1].pop())
            amount -= 1
        stacks[to_index - 1] += elements[::-1]
top = []
for stack in stacks:
    top.append(stack[-1][1])
print("".join(top))
