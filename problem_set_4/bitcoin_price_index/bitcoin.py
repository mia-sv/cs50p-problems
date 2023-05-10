import sys
import requests

try:
    n = float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit("Not a number. Try again.")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    sys.exit("Request failed.")

price = response["bpi"]["USD"]["rate_float"] * n

print(f"${price:,.4f}")
