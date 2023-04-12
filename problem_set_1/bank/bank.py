def main():
    greeting = input("Greeting: ").lower().strip()

    if hello_greet(greeting):
        print("$0")
    elif h_greet(greeting):
        print("$20")
    else:
        print("$100")


def hello_greet(x):
    return x.startswith("hello")

def h_greet(x):
    return x[0] == "h"

main()