import sys

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

input_csv = sys.argv[1]
output_csv = sys.argv[2]

if input_csv[-4:] != ".csv":
    print(f"Could not read {input_csv}")
    sys.exit(1)

try:
    input_file = open(input_csv, "r")
    input_lines = input_file.readlines()

    students = []
    students.append("first,last,house")

    for line in input_lines[1:]:
        split_line = line[:-1].replace('"', "").replace(" ", "").split(",")

        first_name = split_line[1]
        last_name = split_line[0]
        house = split_line[2]

        students.append(f"{first_name},{last_name},{house}")

    input_file.close()

    output_file = open(output_csv, "w")

    for student in students:
        output_file.write(student)
        output_file.write("\n")

    output_file.close()

except OSError:
    print(f"Could not read {input_csv}")
    sys.exit(1)
