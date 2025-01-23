from PIL import Image


for numSeq in range(1, 9):
    print("{:03d}".format(numSeq))
    im = Image.open("{:03d}".format(numSeq) + ".pgm" + ".pgm")
    im.save("{:03d}".format(numSeq) + ".png")

