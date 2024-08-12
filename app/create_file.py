import sys
import os
import datetime


if "-d" in sys.argv and "-f" in sys.argv:
    directories = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
    path = os.path.join(*directories)
    os.makedirs(path)

    file_path = os.path.join(path, sys.argv[sys.argv.index("-f") + 1])
else:
    file_path = sys.argv[sys.argv.index("-f") + 1]

with open(file_path, "a") as file:
    file.write(str(datetime.datetime.now()) + "\n")
    while True:
        content = input("Enter content line: ")
        if content.lower() == "stop":
            break
        file.write(content + "\n")

    file.write("\n")
