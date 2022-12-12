from collections import deque
from typing import Tuple

graph = []
end = (-1, -1)
row_index = 0
starts = []

for line in open("input.txt", "r"):
    graph.append(list(line.strip()))
    if "S" in graph[-1]:
        col_index = graph[-1].index("S")
        start = (row_index, col_index)
        graph[row_index][col_index] = "a"

    for col_index, letter in enumerate(graph[-1]):
        if letter == "a":
            starts.append((row_index, col_index))

    if "E" in graph[-1]:
        col_index = graph[-1].index("E")
        end = (row_index, col_index)
        graph[row_index][col_index] = "z"

    row_index += 1


def is_valid(coord: Tuple[int, int]) -> bool:
    row, col = coord
    return 0 <= row < len(graph) and 0 <= col < len(graph[0])


def bfs():
    queue = deque(starts)
    visited = set(starts)
    direction = [-1, 0, 1, 0, -1]
    level = 0

    while queue:
        size = len(queue)

        while size:
            parent = queue.popleft()
            parent_row, parent_col = parent
            parent_char = graph[parent_row][parent_col]

            if parent == end:
                print(level)
                queue.clear()
                return

            for index in range(1, len(direction)):
                new_coord = (parent_row + direction[index - 1], parent_col + direction[index])
                (row, col) = new_coord
                if is_valid(new_coord) and new_coord not in visited:
                    char = graph[row][col]
                    if ord(char) - ord(parent_char) <= 1:
                        visited.add(new_coord)
                        queue.append(new_coord)
            size -= 1
        level += 1


bfs()
