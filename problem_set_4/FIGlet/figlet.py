from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font = ""

match sys.argv:
    case [_]:
        fonts = figlet.getFonts()
        font = random.choice(fonts)
    case [_, "-f" | "--font", font_name]:
        font = font_name
    case _:
        print("Wrong number of arguments")
        exit(1)

figlet.setFont(font=font)

user_input = input("Input: ")

print("Output:")
print(figlet.renderText(user_input))
