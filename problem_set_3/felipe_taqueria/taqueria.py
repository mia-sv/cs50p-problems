menu: dict[str, float] = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00,
}

total: float = 0

while True:
    try:
        item: str = input("Item: ").lower()
        if item in menu:
            total += menu[item]
            print("Total: $%.2f" % total)

    except (IndexError, ValueError):
        continue
    except EOFError:
        break
