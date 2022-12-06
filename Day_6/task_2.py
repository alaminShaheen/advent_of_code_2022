for line in open("input.txt", "r"):
    line = line.strip()
    left = 0
    window = set()
    for right in range(len(line)):
        while line[right] in window:
            window.remove(line[left])
            left += 1

        window.add(line[right])

        if len(window) == 14:
            print(right + 1)
            break
