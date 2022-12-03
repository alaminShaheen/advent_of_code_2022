max_calorie = current_calorie = 0
#          R       P       S
points = {"X": 1, "Y": 2, "Z": 3}
score = 0

for line in open("input.txt", "r"):
    line = line.strip()
    oppo, me = line.split(" ")

    if me == "Y":
        score += 3
        if oppo == "A":
            score += points["X"]
        elif oppo == "B":
            score += points["Y"]
        else:
            score += points["Z"]
    elif me == "Z":
        score += 6
        if oppo == "A":
            score += points["Y"]
        elif oppo == "B":
            score += points["Z"]
        else:
            score += points["X"]
    else:
        if oppo == "A":
            score += points["Z"]
        elif oppo == "B":
            score += points["X"]
        else:
            score += points["Y"]

print(score)
