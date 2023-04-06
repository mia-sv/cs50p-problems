def main():
    user_input = input("Insert something with a face: ")

    new_input = convert(user_input)

    print(new_input)


def convert(text: str):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()


