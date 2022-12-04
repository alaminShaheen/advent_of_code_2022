
overlaps = 0
for line in open("input.txt", "r"):
    line: str = line.strip()
    elf1, elf2 = line.split(",")
    elf1_start, elf1_end = list(map(int, elf1.split("-")))
    elf2_start, elf2_end = list(map(int, elf2.split("-")))

    if elf1_end < elf2_start or elf1_start > elf2_end or \
            elf2_end < elf1_start or elf2_start > elf1_end:
        continue
    else:
        overlaps += 1
print(overlaps)
