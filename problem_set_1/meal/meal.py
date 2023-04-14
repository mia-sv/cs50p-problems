def main():
    time = input("What time is it? ")

    time_in_decimal = convert(time)

    if time_in_decimal >= 7.0 and time_in_decimal <= 8.0:
        print("breakfast time")
    elif time_in_decimal >= 12.0 and time_in_decimal <= 13.0:
        print("lunch time")
    elif time_in_decimal >= 18.0 and time_in_decimal <= 19.0:
        print("dinner time")


def convert(time):
    time_list = time.split(" ")
    is_12 = len(time_list) == 2
    is_am = time_list[-1] == "a.m."
    h, m = time_list[0].split(":")

    m_in_decimal = int(m) / 0.6 * 0.01
    result = float(h) + m_in_decimal

    if h == "12" and is_am:
        result = m_in_decimal
    elif h != "12" and not is_am and is_12:
        result += 12.0  # result = result + 12

    return result


if __name__ == "__main__":
    main()
