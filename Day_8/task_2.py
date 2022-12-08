import math

grid = []


def find_visibility(row: int, col: int) -> int:
    tree = grid[row][col]

    top = left = right = bottom = 0
    for c in range(col + 1, len(grid[0])):
        right += 1
        if grid[row][c] >= tree:
            break

    for c in range(col - 1, -1, -1):
        left += 1
        if grid[row][c] >= tree:
            break

    for r in range(row + 1, len(grid)):
        bottom += 1
        if grid[r][col] >= tree:
            break

    for r in range(row - 1, -1, -1):
        top += 1
        if grid[r][col] >= tree:
            break
    return top * right * bottom * left


for line in open("input.txt", "r"):
    line = list(map(int, list(line.strip())))
    grid.append(line)

max_visibility = -math.inf
for row in range(len(grid)):
    for col in range(len(grid[0])):
        max_visibility = max(max_visibility, find_visibility(row, col))

print(max_visibility)
