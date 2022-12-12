import sys

file_name, content = sys.argv[1], sys.argv[2]
with open(file_name, "w") as f:
    f.write(content)