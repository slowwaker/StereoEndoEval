from PIL import Image

for x in range(11,16):
    img = Image.open("{:03d}".format(x) + ".png").convert("L")
    img.save("{:03d}".format(x) + "_grey.png")

for x in range(80,85):
    img = Image.open("{:03d}".format(x) + ".png").convert("L")
    img.save("{:03d}".format(x) + "_grey.png")

for x in range(90,95):
    img = Image.open("{:03d}".format(x) + ".png").convert("L")
    img.save("{:03d}".format(x) + "_grey.png")

# img = Image.open("001.png").convert("L")
# img.save("001_grey.png")


# img = Image.open("000240"+"_right.png").convert("L")
# img.save("000240"+"grey_right.png")

# img = Image.open("004110"+"_left.png").convert("L")
# img.save("004110"+"grey_left.png")


# img = Image.open("004110"+"_right.png").convert("L")
# img.save("004110"+"grey_right.png")

# img = Image.open("006720"+"_left.png").convert("L")
# img.save("006720"+"grey_left.png")


# img = Image.open("006720"+"_right.png").convert("L")
# img.save("006720"+"grey_right.png")
# for numSeq in range(1, 9):
#     print("{:03d}".format(numSeq))
#     im = Image.open("{:03d}".format(numSeq) + ".png")
#     im.save("{:03d}".format(numSeq) + ".pgm")

