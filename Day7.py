class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.sub_directories = []
        self.files = {}


class Filesystem:
    def create_dir(self, name, parent):
        return Directory(name, parent)

    def get_dir_name(self, directory):
        return directory.name

    def get_dir_parent(self, directory):
        return directory.parent

    def get_sub_directories(self, directory):
        return directory.sub_directories

    def get_root_dir(self, directory):
        res = directory
        while res.parent is not None:
            res = res.parent
        return res

    def get_dir_size(self, directory):
        return sum(directory.files.values()) + sum(
            [self.get_dir_size(sd) for sd in directory.sub_directories]
        )

    def insert_dir(self, current_dir, name):
        new_dir = self.create_dir(name, current_dir)
        current_dir.sub_directories.append(new_dir)
        return new_dir

    def insert_file(self, directory, file, size):
        directory.files[file] = size


def parse_file_system_tree(fsystem, doc):

    current_directory = None

    with open(doc) as f:
        for line in f:
            line = line.rstrip().split(" ")
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        current_directory = fsystem.get_dir_parent(
                            current_directory
                        )
                    elif line[2] == "/":
                        if current_directory:
                            current_directory = fsystem.get_root_dir(
                                current_directory
                            )
                        else:
                            current_directory = fsystem.create_dir(
                                "/", None
                            )  # initial dir
                    else:
                        current_directory = fsystem.insert_dir(
                            current_directory, line[2]
                        )
                elif line[1] == "ls":
                    pass
                else:
                    print(line[1])
                    print("incorrect command")
                    break
            else:
                if line[0] != "dir":
                    fsystem.insert_file(current_directory, line[1], int(line[0]))

    return current_directory


def get_dirs_of_atmost_100k(fs, directory):
    dir_size = fs.get_dir_size(directory)

    if dir_size <= 100000:
        if not fs.get_sub_directories(directory):
            return dir_size
        else:
            return dir_size + sum(
                [
                    get_dirs_of_atmost_100k(fs, sd)
                    for sd in fs.get_sub_directories(directory)
                ]
            )
    else:
        return sum(
            [
                get_dirs_of_atmost_100k(fs, sd)
                for sd in fs.get_sub_directories(directory)
            ]
        )


if __name__ == "__main__":
    doc = "./Day7_input.txt"
    fsystem = Filesystem()
    cdir = parse_file_system_tree(fsystem, doc)
    root = fsystem.get_root_dir(cdir)
    response = get_dirs_of_atmost_100k(fsystem, root)
    print(f"response: {response}")
