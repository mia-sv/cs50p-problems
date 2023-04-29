MONTHS: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    try:
        input_date: str = input("Date: ")
        split_date: list[str] = input_date.split("/")
        day: int = 0
        month: int = 0
        year: int = 0

        if len(split_date) == 3:
            month = int(split_date[0])
            if not 0 < month < 13:
                continue

            day = int(split_date[1])
        else:
            split_date = input_date.split(" ")
            
            if len(split_date) == 3:
                if split_date[1][-1] != ",":
                    continue

                month = MONTHS.index(split_date[0]) + 1
                day = int(split_date[1].replace(",", ""))
            else:
                continue

        if not 0 < day < 32:
            continue

        year = int(split_date[2])
        if not 999 < year < 10000:
            continue

        print(f"{year}-{month:02}-{day:02}")
        break
    except:
        continue
