from datetime import date
from typing import Annotated
import inflect
import sys

def main():
    try:
        user_date = input("Date of Birth: ")
        print(f"{date_to_minutes(user_date)} minutes")

    except ValueError:
        print("Invalid date")
        sys.exit(1)


def date_to_minutes(d):
    parsed_date = date.fromisoformat(d)
    interval = date.today() - parsed_date
    interval_in_minutes = int(interval.total_seconds() / 60)

    p = inflect.engine()
    interval_in_words = p.number_to_words(interval_in_minutes, andword="")

    return interval_in_words.capitalize()


if __name__ == "__main__":
    main()
