import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\b(um)\b", s.lower())

    if matches:
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()
