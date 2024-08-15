from __future__ import annotations
import argparse
from datetime import datetime
import os


def create_path(directories: list | None, filename: str | None) -> str:
    if directories:
        path_dir = os.path.join(*directories)
        os.makedirs(path_dir, exist_ok=True)

        if filename:
            return os.path.join(path_dir, filename)
    return filename


def make_content() -> list:
    content_list = [datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n", ]
    line_number = 1
    while True:
        content = input("Enter content line: ")
        if content.lower() == "stop":
            content_list.append("\n")
            break
        content_list.append(str(line_number) + " " + content + "\n")
        line_number += 1

    return content_list


def create_file(file_path: str) -> None:
    content = make_content()
    try:
        user_file = open(file_path, "a")
        user_file.writelines(content)
    except Exception as e:
        print(e)
    finally:
        user_file.close()


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
    path = create_path(args.directories, args.file)

    if args.file:
        create_file(path)


if __name__ == "__main__":
    main()
