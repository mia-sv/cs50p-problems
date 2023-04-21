def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False

    if not s.isupper():
        return False

    if len(s) > 6 or len(s) < 2:
        return False

    if s.isdigit() or (s[0].isdigit() and s[1].isdigit()):
        return False

    for i in range(0, len(s)):
        if i + 1 < len(s) and s[i].isdigit() and s[i + 1].isalpha():
            return False

        if i > 0 and s[i] == "0" and s[i - 1].isalpha():
            return False

    return True

main()
