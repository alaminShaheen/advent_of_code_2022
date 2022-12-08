row = 0
for line in open("input.txt", "r"):
    line = list(map(int, line.strip().split()))
    left, right = 0, len(line) - 1
    visible_trees = 0
    visible_trees_coord = set()
    left_big, right_big = line[left], line[right]

    while left < len(line) or right >= 0:
        if (row, left) not in visible_trees_coord or left == 0 or line[left] > left_big:
            visible_trees += 1
            left_big = max(left_big, line[left])
            visible_trees_coord.add((row, left))
            continue
        else:
            left_big = math.inf

        if (row, right) not in visible_trees_coord or right == len(line) - 1 or line[right] > right_big:
            visible_trees += 1
            right_big = max(right_big, line[right])
            visible_trees_coord.add((row, right))
            continue
        else:
            right_big = math.inf
        left += 1
        right -= 1
    row += 1
