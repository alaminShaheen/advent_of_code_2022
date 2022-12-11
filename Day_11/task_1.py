from collections import defaultdict

line_index = 0
test_monkeys = []
monkey_items = defaultdict(list)
monkey_operations = {}
monkey_test = {}
monkey_throw = defaultdict(list)
monkey_inspect = defaultdict(int)

for line in open("input.txt", "r"):
    if line_index % 7 == 0:
        monkey_index = int(line.strip()[-2])
    elif line_index % 7 == 1:
        _, starting_items = line.strip().split(": ")
        monkey_items[monkey_index] = list(map(int, starting_items.split(", ")))
    elif line_index % 7 == 2:
        _, operation = line.strip().split(": ")
        operation = operation.split()
        operation_sign, operation_value = operation[-2], operation[-1]
        if operation_value.isdigit():
            operation_value = int(operation_value)
        monkey_operations[monkey_index] = [operation_sign, operation_value]
    elif line_index % 7 == 3:
        monkey_test[monkey_index] = int(line.strip().split()[-1])
    elif line_index % 7 in [4, 5]:
        monkey_throw[monkey_index].append(int(line.strip().split()[-1]))
    else:
        pass
    line_index += 1

rounds, monkey_index = 1, 0
top = bottom = -1

for rounds in range(20):
    for monkey_index in range(len(monkey_items.keys())):
        for item in monkey_items[monkey_index]:
            monkey_inspect[monkey_index] += 1
            worry_level = item

            operation_sign, operation_value = monkey_operations[monkey_index]
            operation_value = operation_value if isinstance(operation_value, int) else worry_level
            if operation_sign == "+":
                worry_level += operation_value
            else:
                worry_level *= operation_value

            worry_level //= 3
            if worry_level % monkey_test[monkey_index] == 0:
                monkey_items[monkey_throw[monkey_index][0]].append(worry_level)
            else:
                monkey_items[monkey_throw[monkey_index][1]].append(worry_level)
        monkey_items[monkey_index] = []


for inspection in monkey_inspect.values():
    if inspection > top:
        bottom = top
        top = inspection
    elif inspection > bottom:
        bottom = inspection

print(top * bottom)
