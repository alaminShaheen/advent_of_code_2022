max_calorie_1 = max_calorie_2 = max_calorie_3 = current_calorie = 0

for line in open("input.txt", "r"):
    line = line.strip()
    if line:
        current_calorie += int(line)
    else:
        if current_calorie > max_calorie_1:
            max_calorie_3 = max_calorie_2
            max_calorie_2 = max_calorie_1
            max_calorie_1 = current_calorie
        elif current_calorie > max_calorie_2:
            max_calorie_3 = max_calorie_2
            max_calorie_2 = current_calorie
        elif current_calorie > max_calorie_3:
            max_calorie_3 = current_calorie
        current_calorie = 0
print(max_calorie_1 + max_calorie_2 + max_calorie_3)
