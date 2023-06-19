import sys
from PIL import Image
from PIL import ImageOps


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if (
    input_file[-4:] != ".jpg"
    and input_file[-4:] != ".png"
    and input_file[-5:] != ".jpeg"
):
    print("Invalid output")
    sys.exit(1)

split_input_file = input_file.split(".")
split_output_file = output_file.split(".")

if split_input_file[1] != split_output_file[1]:
    print("Input and output have different extensions")
    sys.exit(1)


try:    
    shirt = Image.open("shirt.png", mode="r")
    image: Image = Image.open(input_file, mode="r")
    image = ImageOps.fit(image, size=shirt.size)
    image.paste(shirt, shirt)
    image.save(output_file)


except OSError:
    print(f"Could not read {input_file}")
    sys.exit(1)
