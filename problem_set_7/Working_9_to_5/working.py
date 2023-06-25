import re


def main():
    print(convert(input("Hours: ")))


def format_time(unformatted_time):
    match = re.search(
        r"^([1-9]|(?:1[0-2]))(?:\:([0-5][0-9])?)? (AM|PM)$", unformatted_time
    )

    if not match:
        return None

    is_pm = match.group(3) == "PM"
    hour = int(match.group(1))
    minutes = match.group(2)

    if not minutes:
        minutes = "00"

    if is_pm:
        return f"{(hour % 12) + 12}:{minutes}"
    else:
        if hour not in [10, 11]:
            return f"0{hour % 12}:{minutes}"
        else:
            return f"{hour}:{minutes}"


def convert(s):
    split_s = s.split(" to ")

    if len(split_s) != 2:
        raise ValueError
        sys.exit(1)

    time1 = format_time(split_s[0])
    time2 = format_time(split_s[1])

    if not time1 or not time2:
        raise ValueError
        sys.exit(1)

    return f"{time1} to {time2}"


if __name__ == "__main__":
    main()
