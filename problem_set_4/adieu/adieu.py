names = []

while True:
    try:
        input_name = input("Name: ")
        names.append(input_name)
    except EOFError:
        break

song = "Adieu, adieu, to "

for names_i in range(len(names)):
    name = names[names_i]

    match names_i:
        case 0:
            song += name
        case 1 if len(names) == 2:
            song += " and " + name
        case _ if names_i == (len(names) - 1):
            song += ", and " + name
        case _:
            song += ", " + name

print()
print(song)
