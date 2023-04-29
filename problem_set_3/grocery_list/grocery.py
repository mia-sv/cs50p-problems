grocery_list: dict[str, int] = {}


while True:
    try:
        item: str = input("").upper()

        if item not in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1

    except EOFError:
        sorted_grocery_list = dict(sorted(grocery_list.items()))
        for item in sorted_grocery_list:
            print(sorted_grocery_list[item], item)
        break


