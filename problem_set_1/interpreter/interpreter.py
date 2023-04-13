calc = input("Expression: ").strip()

x, y, z = calc.split(" ")

new_calc = (calc.split(" "))

int_x = int(x)

int_z = int(z)
    


match new_calc [1]:
    case "+":
        print(float(int_x + int_z))
    case "-":
        print(float(int_x - int_z))
    case "*":
        print(float(int_x * int_z))
    case _:
        print(float(int_x / int_z))












