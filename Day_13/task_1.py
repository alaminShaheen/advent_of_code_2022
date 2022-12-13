import string


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


row_index = valid_pairs = 0
pair_index = 1
pair = []

for line in open("input.txt", "r"):
    if line.strip():
        pair.append(form_array(line.strip()))
        if len(pair) == 2:
            result = arr_compare(pair[0], pair[1])
            if result > 0:
                valid_pairs += pair_index
            pair.clear()
            pair_index += 1
    row_index += 1

print(valid_pairs)
