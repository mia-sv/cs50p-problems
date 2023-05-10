import random


def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = str(x + y)
        tries_left = 3

        while tries_left > 0:
            guess = input(f"{x} + {y} = ")

            if guess == answer:
                correct_answers += 1
                break

            print("EEE")
            tries_left -= 1

            if tries_left == 0:
                print(f"{x} + {y} = {answer}")

    print(f"Score: {correct_answers}")


def get_level():
    while True:
        level = input("Level: ")

        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
