import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

csv_path = sys.argv[1]

if csv_path[-4:] != ".csv":
    print("Not a CSV file")
    sys.exit(1)

try:
    csv_file = open(csv_path, "r")
    csv_lines = csv_file.readlines()

    menu = []
    for csv_line in csv_lines:
        menu.append(csv_line[:-1].split(","))

    print(tabulate(menu, headers="firstrow", tablefmt="grid"))

except OSError:
    print("File does not exist")
    sys.exit(1)
