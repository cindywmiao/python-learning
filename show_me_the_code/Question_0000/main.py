import Image
import ImageFont
import ImageDraw

text = u"15"

im = Image.open('./image.jpg')

dr = ImageDraw.Draw(im)
font = ImageFont.truetype('msyh.ttf', 34)

dr.text((im.size[0]*0.75, im.size[1]*0.05), text, font=font, fill="#ff0000")

im.show()
im.save('result.jpg')