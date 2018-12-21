from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# font_path = 'C:/Windows/Fonts/Georgia.ttf'
# 随机字母
def random_char():
    return chr(random.randint(65, 90))
# 随机数字
def random_num():

    return random.randint(0, 9)

# 随机字体颜色  稍深
def random_color():
    return (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))


# 随机背景颜色
def random_color2():
    return (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120))

# 生成背景图层
image = Image.new('RGB',size=(240, 60), color=(255, 255, 255))

# # 显示图片
# image.show()
# 生成绘制对象
draw = ImageDraw.Draw(image)
#定义要使用的字体
font = ImageFont.truetype('arial.ttf', 36)

 # 循环像素点并填充颜色
for x in range(0, 240):
    for y in range(0, 60):
        draw.point(xy=(x, y), fill=random_color2())
# 生成文字
for t in range(0, 4):
    draw.text((60*t + 20, 10), random_char(), font=font, fill=random_color())
# 加模糊滤镜
image = image.filter(ImageFilter.BLUR)

# 干扰
# draw.point([100,100],pill="red")
# draw.point([80,80],fill=(0,0,0))
# draw.line((100,100),fill="red")
# draw.line((100,200),fill="blue")
# draw.arc((100,100),0,360,fill="red")
# draw.arc((0,0),0,90,fill="blue")
# 生成图片并保存
with open('demo5.jpg', 'wb')as f:
    image.save(f, format='jpeg')







# import random
#
# from PIL import Image,ImageDraw,ImageFont,ImageFilter
# #字体的位置，不同版本的系统会有不同BuxtonSketch.ttf
# font_path = 'C:/Windows/Fonts/Georgia.ttf'
# #生成几位数的验证码
# number = 4
# #生成验证码图片的高度和宽度
# size = (129,53)
# #背景颜色，默认为白色
# bgcolor = (255,255,255)
# #字体颜色，默认为蓝色
# fontcolor = (0,0,0)
# #干扰线颜色。默认为红色
# linecolor = (0,0,0)
# #是否要加入干扰线
# draw_line = True
# #加入干扰线条数的上下限
# line_number = (1,5)
#
# #用来随机生成一个字符串
# def gene_text():
#     # source = list(string.letters)
#     # for index in range(0,10):
#     #     source.append(str(index))
#     source = ['0','1','2','3','4','5','6','7','8','9']
#     # source = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J', 'K','L', 'M', 'N','O','P','Q','R',
#     #           'S', 'T', 'U', 'V', 'W', 'Z','X', 'Y']
#     return ''.join(random.sample(source,number))#number是生成验证码的位数
# #用来绘制干扰线
# def gene_line(draw,width,height):
#     # begin = (random.randint(0, width), random.randint(0, height))
#     # end = (random.randint(0, width), random.randint(0, height))
#     begin = (0, random.randint(0, height))
#     end = (74, random.randint(0, height))
#     draw.line([begin, end], fill = linecolor,width=3)
#
# #生成验证码
# def gene_code():
#     width,height = size #宽和高
#     image = Image.new('RGB',(width,height),bgcolor) #创建图片
#     font = ImageFont.truetype(font_path,40) #验证码的字体
#     draw = ImageDraw.Draw(image)  #创建画笔
#     text = gene_text() #生成字符串
#     font_width, font_height = font.getsize(text)
#     draw.text(((width - font_width) / number, (height - font_height) / number),text,\
#             font= font,fill=fontcolor) #填充字符串
#     if draw_line:
#         gene_line(draw,width,height)
#     image = image.transform((width+30,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
#     # image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
#     image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
#     # a = str(m)
#     aa = str(".png")
#     path = font_path + text + aa
#     # cv2.imwrite(path, I1)
#     image.save('idencode.jpg', 'jpeg') #保存验证码图片
#     # image.save(path)
# x=1
# # if __name__ == "__main__":
# # for k in(1,1000):
# while x<20:
#      gene_code()
#      x+=1
