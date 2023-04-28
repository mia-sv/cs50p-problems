def main():
    fuel_left: int = parse_input()

    if fuel_left <= 1:
        print("E")
    elif fuel_left >= 99:
        print("F")
    else:
        print(f"{fuel_left}%")


def parse_input() -> int:
    while True:
        try:
            user_input: str = input("Fraction: ")

            if "." in user_input:
                continue

            split_input: list[str] = user_input.split("/")

            x: int = int(split_input[0])
            y: int = int(split_input[1])

            if x > y:
                continue

            result: float = x / y * 100

            return round(result)

        except (IndexError, ValueError, ZeroDivisionError):
            continue


main()
