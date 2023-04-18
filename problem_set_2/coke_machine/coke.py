amount_due = 50
accepted_coins = [5, 10, 25]

while True:
    print(f"Amount Due: {amount_due}")
    inserted_coin = int(input("Insert coin: "))

    if inserted_coin in accepted_coins:
        amount_due -= inserted_coin

        if amount_due <= 0:
            print(f"Change Owed: {-amount_due}")
            break
