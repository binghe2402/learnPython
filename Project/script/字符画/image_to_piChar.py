'''图片转字符画'''

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', default='output.txt')
parser.add_argument('-height', type=int, default=None)
parser.add_argument('-weight', type=int, default=None)

args = parser.parse_args()

H = args.height
W = args.weight
FILE = args.file
OUTPUT = args.o


ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def pix_to_char(pixel):
    if len(pixel) > 1:
        r, g, b = pixel[0], pixel[1], pixel[2]
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    else:
        gray = pixel[0]

    char = ascii_char[int(gray/255*len(ascii_char))]
    return char


if __name__ == '__main__':
    im = Image.open(FILE)
    if H and W:
        im = im.resize((W, H), Image.NEAREST)
    else:
        W, H = im.size

    pixChar = ''
    for i in range(H):
        for j in range(W):
            pix = im.getpixel((j, i))
            pixChar += pix_to_char(pix)

        pixChar += '\n'

    print(pixChar)

    with open(OUTPUT, 'w') as f:
        f.write(pixChar)
