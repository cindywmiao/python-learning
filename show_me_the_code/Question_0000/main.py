import Image
import ImageFont
import ImageDraw
import argparse

text = u"15"

def change_image(input_path, output_path):
    im = Image.open(input_path)
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype('msyh.ttf', 34)
    dr.text((im.size[0] * 0.75, im.size[1] * 0.05), text, font=font, fill="#ff0000")
    im.slow()
    im.save(output_path)


def main():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-i', '--input', help='Description for foo argument', required=True)
    parser.add_argument('-o', '--output', help='Description for bar argument', required=True)
    args = vars(parser.parse_args())
    change_image(args['input'], args['output'])

if __name__ == '__main__':
    main()

