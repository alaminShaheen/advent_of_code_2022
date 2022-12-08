import math


class File:
    def __init__(self, name, size, parent_directory):
        self.name = name
        self.size = size
        self.parent = parent_directory
        self.type = "file"


class Directory(File):
    def __init__(self, name, size, parent_directory, children=None):
        super().__init__(name, size, parent_directory)
        self.children = children if children is not None else {}
        self.type = "directory"


limit, disk_space = 100000, 70000000
root_dir = Directory("/", 0, None, {})
parent_dir: Directory = None
current_dir: Directory = root_dir

for line in open("input.txt", "r"):
    instruction = line.strip().split(" ")

    if instruction[0] == "$":
        if instruction[1] == "cd":
            _, command, destination = instruction

            if destination == "..":
                current_dir = current_dir.parent
            else:
                current_dir = root_dir if root_dir.name == destination else current_dir.children[destination]
            parent_dir = current_dir.parent
    else:
        if instruction[0] == "dir":
            _, directory_name = instruction
            directory = Directory(directory_name, 0, current_dir, {})
            current_dir.children[directory.name] = directory
        else:
            # print(instruction, current_dir.name, parent_dir.name if parent_dir is not None else None)
            file_size, file_name = instruction
            file = File(file_name, int(file_size), current_dir)
            current_dir.children[file.name] = file

directory_sizes = []


def get_dir_sizes(directory: Directory):
    dir_size = 0
    for file in directory.children.values():
        if file.type == "file":
            dir_size += file.size
        else:
            dir_size += get_dir_sizes(file)
    directory.size = dir_size

    directory_sizes.append(directory.size)

    return directory.size


get_dir_sizes(root_dir)

meen = math.inf
for size in directory_sizes:
    if disk_space - root_dir.size + size >= 30000000:
        meen = min(meen, size)

print(meen)
