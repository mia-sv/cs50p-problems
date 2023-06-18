def main():
    while True:
        try:
            fraction: str = input("Fraction: ")
            fuel_left: int = convert(fraction)
            break

        except (IndexError, ValueError, ZeroDivisionError):
            continue

    print(gauge(fuel_left))


def convert(fraction: str) -> int:
    if "." in fraction:
        raise ValueError

    split_fraction: list[str] = list(filter(lambda n: n != "", fraction.split("/")))

    if len(split_fraction) != 2:
        raise IndexError

    x: int = int(split_fraction[0])
    y: int = int(split_fraction[1])

    if x > y:
        raise ValueError

    result: float = x / y * 100

    return round(result)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
