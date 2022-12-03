ssum = index = 0
rucksack_1 = set()

for line in open("input.txt", "r"):
    line: str = line.strip()
    if index % 3 < 3:
        rucksack_1 = rucksack_1.intersection(set(line)) if bool(rucksack_1) else set(line)

    if index % 3 == 2:
        ans = list(rucksack_1)[0]
        if ans.islower():
            ssum += ord(ans) - ord("a") + 1
        else:
            ssum += ord(ans) - ord("A") + 27
        rucksack_1.clear()
    index += 1
print(ssum)
