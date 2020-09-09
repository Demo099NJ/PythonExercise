# filename: generation.py

from PIL import Image

picture = Image.open("picture.jpg")

width = 1080
height = 2280
compress_im = picture.resize((1080, 2280), Image.NEAREST)

pixel = compress_im.load()
template = [8, 0, 0]
for x in range(0, width):
	for y in range(0, height):
		for z in range(0, 3):
			print pixel[x, y]
			#compress_im[x, y][z] = template[z]

compress_im.save("compress_image.jpg")

picture.close()
