import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(
        r"^([12]?\d?\d+)\.([12]?\d?\d+)\.([12]?\d?\d+)\.([12]?\d?\d+)$", ip
    )

    return (
        matches is not None
        and int(matches.group(1)) <= 255
        and int(matches.group(2)) <= 255
        and int(matches.group(3)) <= 255
        and int(matches.group(4)) <= 255
    )


if __name__ == "__main__":
    main()
