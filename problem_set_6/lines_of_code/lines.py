import sys

line_checker = lambda line: len(line.strip()) != 0 and line.strip()[0] != "#"

if len(sys.argv) != 2:
    print("Too few command-line arguments")
    sys.exit(1)

program = sys.argv[1]

if program[-3:] != ".py":
    print("Not a Python file")
    sys.exit(1)

try:
    program_file = open(program, "r")
    program_lines = program_file.readlines()
    checked_lines = list(filter(line_checker, program_lines))
    print(len(checked_lines))
    program_file.close()

except OSError:
    print("File does not exist")
    sys.exit(1)

