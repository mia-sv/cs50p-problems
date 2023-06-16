vowels = ["a", "e", "i", "o", "u"]


def main():
    name = input("Input: ")
    print(f"Output: {shorten(name)}")


def shorten(word):
    new_word = word

    for x in vowels:
        new_word = new_word.replace(x, "").replace(x.upper(), "")
    return new_word


if __name__ == "__main__":
    main()
