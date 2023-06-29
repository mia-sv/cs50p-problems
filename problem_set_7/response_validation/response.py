import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(e):
    valid_email = validators.email(e)

    if valid_email:
        return "Valid"

    else:
        return "Invalid"


if __name__ == "__main__":
    main()
