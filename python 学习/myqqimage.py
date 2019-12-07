from PIL import Image,ImageDraw,ImageFont

sourceFileName = "../public/source.png"
starimg = Image.open(sourceFileName)
drawstarimg = ImageDraw.Draw(starimg)

xsize,ysize =starimg.size
print(xsize,ysize)

fontSize = min(xsize,ysize) // 11
myFont = ImageFont.truetype("Library/Fonts/segoeprb.ttf",fontSize)
drawstarimg.text([0.5 * xsize, 0.5 * ysize],'hello world', fill = (255,16,4),font=myFont)

del drawstarimg
starimg.show()

