grid = []


def find_visibility(row: int, col: int) -> int:
    tree = grid[row][col]

    top = left = right = bottom = 0
    for c in range(col + 1, len(grid[0])):
        if grid[row][c] < tree:
            right += 1
        elif grid[row][c] >= tree:
            right += 1
            break




for line in open("input.txt", "r"):
    line = list(map(int, list(line.strip())))
    grid.append(line)

for row in range(len(grid)):
    for col in range(len(grid[0])):
        find_visibility(row, col)
