from read_file import read_file
from count_frequency import count_frequency


def main():
    line = read_file("input_directory/input.txt")
    for i in count_frequency(line):
        print(i)


if __name__ == "__main__":
    main()
