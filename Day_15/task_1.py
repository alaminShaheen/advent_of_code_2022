from typing import List

sensors, beacons = [], []
ROW = 2000000


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

intervals = []
for sensor, beacon in zip(sensors, beacons):
    sensor_x, sensor_y = sensor
    beacon_x, beacon_y = beacon

    distance = manhattan_distance(sensor, beacon)
    end1 = sensor_x - distance
    end2 = distance + sensor_x

    meen = min(end1, end2)
    maks = max(end1, end2)

    diff = sensor_x - meen
    total_missing = 2 * diff
    upper_bound, lower_bound = sensor_y - diff, sensor_y + diff
    left_bound, right_bound = sensor_x - diff, sensor_x + diff

    if upper_bound <= ROW <= lower_bound:
        row_deviation = abs(sensor_y - ROW)
        left_bound += row_deviation
        right_bound -= row_deviation
        intervals.append([left_bound, right_bound])

merged = []
intervals.sort()
anchor = intervals[0]
for current_index in range(1, len(intervals)):
    anchor_left, anchor_right = anchor
    current_left, current_right = intervals[current_index]
    if anchor_left <= current_left and current_right <= anchor_right:
        pass
    elif anchor_left <= current_left <= anchor_right:
        anchor[1] = current_right
    else:
        merged.append([anchor_left, anchor_right])
        anchor = [current_left, current_right]

    if current_index == len(intervals) - 1:
        merged.append(anchor)

cannot_place = 0
beacons_to_omit = set()
sensors_to_omit = set()
for left, right in merged:
    beacon_count = 0
    for sensor, beacon in zip(sensors, beacons):
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon
        if beacon_y == ROW and left <= beacon_x <= right:
            beacons_to_omit.add(tuple(beacon))
        if sensor_y == ROW and left <= sensor_x <= right:
            sensors_to_omit.add(tuple(sensor))
    cannot_place += right - left + 1
print(cannot_place - len(beacons_to_omit) - len(sensors_to_omit))

