import sys
import os
from datetime import datetime


def create_path() -> str:
    if "-d" in sys.argv and "-f" in sys.argv:
        directories = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        path = os.path.join(*directories)
        os.makedirs(path)

        return os.path.join(path, sys.argv[sys.argv.index("-f") + 1])
    return sys.argv[sys.argv.index("-f") + 1]


def create_file() -> None:
    file_path = create_path()

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
