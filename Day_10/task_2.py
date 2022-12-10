cycle = increment = 0
X = 1

sprite_pos = list("#" * 3 + " " * (40 - 3))

screen = [list(" " * 40) for _ in range(6)]

for line in open("input.txt", "r"):
    instruction = line.strip().split()

    if len(instruction) == 2:
        cycle += 1
        screen[(cycle - 1) // 40][(cycle - 1) % 40] = sprite_pos[(cycle - 1) % 40]
        increment = int(instruction[1])

    cycle += 1
    screen[(cycle - 1) // 40][(cycle - 1) % 40] = sprite_pos[(cycle - 1) % 40]

    if increment:
        X += increment
        increment = 0
        sprite_pos = list(" " * 40)
        for x in range(X - 1, X + 2):
            if 0 <= x < 40:
                sprite_pos[x] = "#"

for row in screen:
    print("".join(row))
