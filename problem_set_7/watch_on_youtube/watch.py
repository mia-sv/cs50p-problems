import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(
        r'^<iframe .*src="https?:\/\/(?:www\.)?youtube\.com\/embed\/([\w-]{11})".*><\/iframe>$',
        s,
    )

    if not matches or len(matches.groups()) != 1:
        return None

    return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
