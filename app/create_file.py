from __future__ import annotations
import argparse
from datetime import datetime
import os


def create_path(directories: list | None, filename: str | None) -> str:
    if directories:
        path_dir = os.path.join(*directories)
        try:
            os.makedirs(path_dir)
            print("<<<Directories created>>>")
        except FileExistsError:
            print("<<<Directories already exists>>>")

        if filename:
            return os.path.join(path_dir, filename)
    return filename


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directories",
        nargs="+",
        help="List of directories"
    )
    parser.add_argument("-f", "--file", type=str, help="Filename")
    args = parser.parse_args()
    print(args)
    path = create_path(args.directories, args.file)

    if args.file:
        create_file(path)


if __name__ == "__main__":
    main()
