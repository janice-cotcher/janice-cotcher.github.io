import os
import sys

filepath = r"sketches"
directory = os.listdir(filepath)
count = 0
for file in directory:
    lines = ""
    try:
        with open(os.path.join(filepath,file), "r") as input:
            lines = input.readlines()
            line_count = len(lines)
    except Exception as e:
        print(e)
        continue

    if not lines:
        print(f"did not output {file}")
        continue

    new_lines = []
    for line in lines:
        if line.strip() == "from processing import *":
            continue
        elif line.strip() == "run()":
            break
        else:
            new_lines.append(line)

    index = 0
    for line in new_lines:
        if line == "" or line == "\n":
            index += 1
        else:
            break

    output = new_lines[index:]

    new_directory = r"new_sketches"
    try:
        with open(file, "w") as f:
            f.writelines(output)
    except Exception as e:
        print(e)
        continue
    print(f"Wrote {file}")
    count += 1

print(f"Successfully wrote{count} files")