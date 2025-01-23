from PIL import Image


for x in range(11,16):
    img = Image.open("{:03d}".format(x) + "_grey.png")
    img.save("{:03d}".format(x) + ".pgm")

for x in range(80,85):
    img = Image.open("{:03d}".format(x) + "_grey.png")
    img.save("{:03d}".format(x) + ".pgm")

for x in range(90,95):
    img = Image.open("{:03d}".format(x) + "_grey.png")
    img.save("{:03d}".format(x) + ".pgm")

# img = Image.open("000240"+"grey_left.png")
# img.save("000240"+"grey_left.pgm")


# img = Image.open("000240"+"grey_right.png")
# img.save("000240"+"grey_right.pgm")

# img = Image.open("004110"+"grey_left.png")
# img.save("004110"+"grey_left.pgm")


# img = Image.open("004110"+"grey_right.png")
# img.save("004110"+"grey_right.pgm")

# img = Image.open("006720"+"grey_left.png")
# img.save("006720"+"grey_left.pgm")


# img = Image.open("006720"+"grey_right.png")
# img.save("006720"+"grey_right.pgm")
# for numSeq in range(1, 9):
#     print("{:03d}".format(numSeq))
#     im = Image.open("{:03d}".format(numSeq) + ".png")
#     im.save("{:03d}".format(numSeq) + ".pgm")

