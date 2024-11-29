# import os


def read_file(path_to_file):
    # if os.path.exists(path_to_file):
    try:
        with open(path_to_file, "r") as f:
            return f.read()
    except (FileNotFoundError, PermissionError):
        print("Error Occured")
        raise


# print(read_file("input_directory/input.txt"))
# read_file("input_directory/file_not_found.txt")
