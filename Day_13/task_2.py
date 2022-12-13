import string
from functools import cmp_to_key


def form_array(arr_str: str):
    stack = []
    num = 0
    for index, char in enumerate(arr_str):
        if char == "[":
            stack.append([])
        elif char in string.digits:
            num = num * 10 + int(char)
        elif char == "," and arr_str[index - 1] in string.digits:
            stack[-1].append(num)
            num = 0
        elif char == "]":
            if arr_str[index - 1] in string.digits:
                stack[-1].append(num)
                num = 0
            arr = stack.pop()
            if stack:
                stack[-1].append(arr)
            else:
                return arr
    return []


def arr_compare(arr1, arr2) -> int:
    p1 = p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        answer = 0
        if isinstance(arr1[p1], int) and isinstance(arr2[p2], int):
            if arr1[p1] != arr2[p2]:
                answer = 1 if arr1[p1] < arr2[p2] else -1
        elif isinstance(arr2[p2], int):
            answer = arr_compare(arr1[p1], [arr2[p2]])
        elif isinstance(arr1[p1], int):
            answer = arr_compare([arr1[p1]], arr2[p2])
        else:
            answer = arr_compare(arr1[p1], arr2[p2])

        if answer:
            return answer
        p1 += 1
        p2 += 1

    return 0 if len(arr1) == len(arr2) else 1 if len(arr1) < len(arr2) else -1


row_index = 0
arrays = []

for line in open("input.txt", "r"):
    if line.strip():
        arrays.append(form_array(line.strip()))
    row_index += 1

divider_1 = "[[6]]"
divider_2 = "[[2]]"

arrays.append(form_array(divider_1))
arrays.append(form_array(divider_2))

arrays.sort(key=cmp_to_key(arr_compare), reverse=True)

result = 1
print(*arrays, sep="\n")
for index, array in enumerate(arrays):
    if len(array) == 1 and array in [[[6]], [[2]]]:
        print(index + 1)
        result *= index + 1
print(result)
