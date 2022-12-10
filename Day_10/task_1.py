cycle = ans = increment = 0
X = 1

for line in open("input.txt", "r"):
    instruction = line.strip().split()
    if len(instruction) == 2:
        cycle += 1
        increment = int(instruction[1])
        if cycle in [20, 60, 100, 140, 180, 220]:
            ans += cycle * X
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        ans += cycle * X
    if increment:
        X += increment
        increment = 0

print(ans)
