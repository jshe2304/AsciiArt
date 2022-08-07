from PIL import Image

raw = Image.open('mona.jpg')

width, height = raw.size

ratio = width/100

img = raw.resize((100, round(height/ratio)))

ascii = ""

for i in range(img.size[1]):
	for j in range(100):

		avg = sum(img.getpixel((j, i)))/3
		
		if avg < 50:
			ascii += "@"
		elif avg < 75:
			ascii += "M"
		elif avg < 100:
			ascii += "w"
		elif avg < 125:
			ascii += "0"
		elif avg < 150:
			ascii += "-"
		else:
			ascii += " "
		
		ascii += " "

	ascii += "\n"

print (ascii)
