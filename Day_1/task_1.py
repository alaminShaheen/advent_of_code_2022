max_calorie = current_calorie = 0

for line in open("input.txt", "r"):
    line = line.strip()
    if line:
        current_calorie += int(line)
    else:
        max_calorie = max(max_calorie, current_calorie)
        current_calorie = 0
print(max_calorie)
