name = input("Input: ")

vowels = ["a", "e", "i", "o", "u"]

for x in vowels:
    name = name.replace(x, "").replace(x.upper(), "")

print(f"Output: {name}")
    