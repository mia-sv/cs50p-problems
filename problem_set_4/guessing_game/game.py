import random

while True:
    try:
        level = int(input("Level: "))

        if level > 0:
            secret = random.randint(1, level)
            break
    except ValueError:
        continue


while True:
    try:
        guess = int(input("Guess: "))

        if guess < 1:
            continue

        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
