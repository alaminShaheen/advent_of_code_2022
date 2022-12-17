from typing import List

sensors, beacons = [], []
bounds = 4000000


def get_coord_value(info: str) -> int:
    value = 0
    negative = False
    for letter in info:
        if letter.isdigit():
            value = value * 10 + int(letter)
        elif letter == "-":
            negative = True
    return -value if negative else value


def manhattan_distance(a: List[int], b: List[int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


for line in open("input.txt", "r"):
    sensor_info, beacon_info = line.strip().split(": ")
    _, _, sensor_x_info, sensor_y_info = sensor_info.split()
    _, _, _, _, beacon_x_info, beacon_y_info = beacon_info.split()
    sensors.append([get_coord_value(sensor_x_info), get_coord_value(sensor_y_info)])
    beacons.append([get_coord_value(beacon_x_info), get_coord_value(beacon_y_info)])

answer_ranges = [[] for _ in range(bounds + 1)]

intervals = [[] for _ in range(bounds + 1)]
ii = 0
for sensor, beacon in zip(sensors, beacons):
    sensor_x, sensor_y = sensor
    beacon_x, beacon_y = beacon

    distance = manhattan_distance(sensor, beacon)
    end1 = sensor_x - distance
    end2 = distance + sensor_x

    meen = min(end1, end2)
    maks = max(end1, end2)

    diff = sensor_x - meen

    upper_bound = sensor_y - diff
    lower_bound = sensor_y + diff

    if 0 <= upper_bound and lower_bound <= bounds:
        pass
    elif upper_bound <= 0 <= lower_bound:
        upper_bound = 0
    elif upper_bound <= bounds <= lower_bound:
        lower_bound = bounds
    else:
        continue

    while upper_bound < lower_bound:
        upper_left_bound = lower_left_bound = sensor_x - diff
        upper_right_bound = lower_right_bound = sensor_x + diff

        upper_row_deviation = abs(sensor_y - upper_bound)
        lower_row_deviation = abs(sensor_y - lower_bound)

        upper_left_bound += upper_row_deviation
        lower_left_bound += lower_row_deviation
        upper_right_bound -= upper_row_deviation
        lower_right_bound -= lower_row_deviation

        if 0 <= upper_left_bound <= upper_right_bound <= bounds:
            intervals[upper_bound].append([upper_left_bound, upper_right_bound])
        elif upper_left_bound <= 0 <= upper_right_bound:
            upper_left_bound = 0
            intervals[upper_bound].append([upper_left_bound, upper_right_bound])
        elif upper_left_bound <= bounds <= upper_right_bound:
            upper_right_bound = bounds
            intervals[upper_bound].append([upper_left_bound, upper_right_bound])
        else:
            pass

        if 0 <= lower_left_bound <= upper_right_bound <= bounds:
            intervals[lower_bound].append([lower_left_bound, lower_right_bound])
        elif lower_left_bound <= 0 <= upper_right_bound:
            lower_left_bound = 0
            intervals[lower_bound].append([lower_left_bound, lower_right_bound])
        elif lower_left_bound <= bounds <= upper_right_bound:
            upper_right_bound = bounds
            intervals[lower_bound].append([lower_left_bound, lower_right_bound])
        else:
            continue

        upper_bound += 1
        lower_bound -= 1
    ii += 1

for ROW, interval in enumerate(intervals):
    merged = []
    interval.sort()
    anchor = interval[0]
    for current_index in range(1, len(interval)):
        anchor_left, anchor_right = anchor
        current_left, current_right = interval[current_index]
        if anchor_left <= current_left and current_right <= anchor_right:
            pass
        elif anchor_left <= current_left <= anchor_right:
            anchor[1] = current_right
        else:
            merged.append([anchor_left, anchor_right])
            anchor = [current_left, current_right]

        if current_index == len(interval) - 1:
            merged.append(anchor)

    for index in range(1, len(merged)):
        _, prev_right = merged[index - 1]
        cur_left, _ = merged[index]
        if cur_left - prev_right == 2:
            print(prev_right + 1, ROW)
            exit()
# 2829680 3411840
