from PIL import Image

img = Image.open('greyscale.png')

x, _ = img.size
l = []
pix = img.getpixel((0,0))
l.append(pix[0])

for i in xrange(4,x,7):
	pix = img.getpixel((i,0))
	l.append(pix[0])

print "".join(chr(ch) for ch in l)
