cave = []
max_col, max_row = 500, 0
rock_ranges = []

for line in open("input.txt", "r"):
    rock_coords = line.strip().split(" -> ")

    for ii in range(1, len(rock_coords)):
        from_col, from_row = list(map(int, rock_coords[ii - 1].split(",")))
        to_col, to_row = list(map(int, rock_coords[ii].split(",")))
        rock_ranges.append([from_col, from_row, to_col, to_row])
        max_col = max(max_col, to_col, from_col)
        max_row = max(max_row, to_row, from_row)

cave = [["." for _ in range(max_col * 2)] for _ in range(max_row + 2 + 1)]

for index in range(len(cave[-1])):
    cave[-1][index] = "#"

for rock_range in rock_ranges:
    from_col, from_row, to_col, to_row = rock_range

    if from_row == to_row:
        for col in range(min(from_col, to_col), max(to_col, from_col) + 1):
            cave[from_row][col] = "#"
    else:
        for row in range(min(from_row, to_row), max(to_row, from_row) + 1):
            cave[row][from_col] = "#"


def simulate_flood_fill():
    r, c = 0, 500
    settled_sands = 0
    while cave[r][c] == ".":
        while r + 1 < len(cave):
            if cave[r + 1][c] == ".":
                pass
            elif c - 1 >= 0 and cave[r + 1][c - 1] == ".":
                c -= 1
            elif c + 1 < len(cave[r + 1]) and cave[r + 1][c + 1] == ".":
                c += 1
            else:
                cave[r][c] = "o"
                settled_sands += 1
                break
            r += 1
        r, c = 0, 500
    return settled_sands


print(simulate_flood_fill())
