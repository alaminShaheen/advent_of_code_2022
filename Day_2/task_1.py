max_calorie = current_calorie = 0
#          R       P       S
points = {"X": 1, "Y": 2, "Z": 3}
score = 0

for line in open("input.txt", "r"):
    line = line.strip()
    oppo, me = line.split(" ")

    if (me == "X" and oppo == "A") \
            or (me == "Y" and oppo == "B") \
            or (me == "Z" and oppo == "C"):
        score += 3
    elif (me == "X" and oppo == "C") \
            or (me == "Y" and oppo == "A") \
            or (me == "Z" and oppo == "B"):
        score += 6
    score += points[me]

print(score)
