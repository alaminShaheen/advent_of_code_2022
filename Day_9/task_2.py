from typing import Tuple

head, tails = (0, 0), [(0, 0) for _ in range(9)]
visited = set([(0, 0)])


def calculate_tail_pos(head_pos: Tuple[int, int], tail_pos: Tuple[int, int]) -> Tuple[int, int]:
    (hx, hy) = head_pos
    (tx, ty) = tail_pos

    if hx == tx:
        if abs(hy - ty) > 1:
            return tx, ty + 1 if hy > ty else ty - 1
    elif hy == ty:
        if abs(hx - tx) > 1:
            return tx + 1 if hx > tx else tx - 1, ty
    elif abs(hx - tx) == abs(hy - ty):
        if abs(hx - tx) == 2:
            return tx + 1 if hx > tx else tx - 1, ty + 1 if hy > ty else ty - 1
    else:
        if abs(hx - tx) == 2:
            return tx + 1 if hx > tx else tx - 1, hy
        else:
            return hx, ty + 1 if hy > ty else ty - 1
    return tail_pos


for line in open("input.txt", "r"):
    direction, distance = line.strip().split()
    distance = int(distance)

    (head_x, head_y) = head

    if direction == "U":
        for y in range(head_y - 1, head_y - distance - 1, -1):
            head = (head_x, y)

            for index in range(len(tails)):
                new = calculate_tail_pos(head if index == 0 else tails[index - 1], tails[index])
                tails[index] = new
                if index == 8:
                    visited.add(tails[index])

    elif direction == "D":
        for y in range(head_y + 1, head_y + distance + 1, 1):
            head = (head_x, y)

            for index in range(len(tails)):
                new = calculate_tail_pos(head if index == 0 else tails[index - 1], tails[index])
                tails[index] = new
                if index == 8:
                    visited.add(tails[index])

    elif direction == "R":
        for x in range(head_x + 1, head_x + distance + 1, 1):
            head = (x, head_y)

            for index in range(len(tails)):
                new = calculate_tail_pos(head if index == 0 else tails[index - 1], tails[index])
                tails[index] = new
                if index == 8:
                    visited.add(tails[index])
    else:
        for x in range(head_x - 1, head_x - distance - 1, -1):
            head = (x, head_y)

            for index in range(len(tails)):
                new = calculate_tail_pos(head if index == 0 else tails[index - 1], tails[index])
                tails[index] = new
                if index == 8:
                    visited.add(tails[index])

print(len(visited))
