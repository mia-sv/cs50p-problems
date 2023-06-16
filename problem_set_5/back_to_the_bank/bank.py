def main():
    greeting = input("Greeting: ").lower().strip()
    print(value(greeting))


def value(x):
    if x.startswith("hello"):
        return 0
    elif x.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
