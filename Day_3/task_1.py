ssum = 0

for line in open("input.txt", "r"):
    line: str = line.strip()
    rucksack_1 = set(line[:len(line) // 2])
    rucksack_2 = set(line[len(line) // 2:])
    ans = list(rucksack_2.intersection(rucksack_1))[0]
    if ans.islower():
        ssum += ord(ans) - ord("a") + 1
    else:
        ssum += ord(ans) - ord("A") + 27
print(ssum)
