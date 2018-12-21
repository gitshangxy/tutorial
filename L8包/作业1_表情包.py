from PIL import Image, ImageDraw, ImageFont

# import os
# img = Image.open('base.png')
img = Image.open('base1.png')

# 生成绘制对象
draw= ImageDraw.Draw(img)

# 字体对象， 字体、字号
font = ImageFont.truetype('simhei.ttf',24)
# draw.text((32, 150),"我的内心毫无波动\n甚至还想笑",fill=(0, 0, 0),font=font)
draw.text((34, 180),"我还能吃 我不胖",fill=(0,0,0),font=font)

img.save('base2.png')
# img.save(".Python生成的表情包.png")
img.show()
# print(os.listdir())

