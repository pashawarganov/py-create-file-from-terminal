import argparse
from datetime import datetime
import os


def create_path() -> str:
    if args.directories:
        path_dir = os.path.join(*args.directories)
        try:
            os.makedirs(path_dir)
            print("<<<Directories created>>>")
        except FileExistsError:
            print("<<<Directories already exists>>>")

        if args.file:
            return os.path.join(path_dir, args.file)
    return args.file


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                file.write("\n")
                break
            file.write(str(line_number) + " " + content + "\n")
            line_number += 1
    print("<<<File created>>>")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directories",
        nargs="+",
        help="List of directories"
    )
    parser.add_argument("-f", "--file", type=str, help="Filename")
    args = parser.parse_args()

    path = create_path()

    if args.file:
        create_file(path)
