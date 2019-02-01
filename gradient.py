def start():
	return "P3\n768 512\n255\n"
def gradient():
	i = 0
	j = 0
	s = ""
	while j < 256:
		while i < 768:
			if i < 256:
				r = 255 - i
				g = i
				b = 0
			elif i < 512:
				r = 0
				g = 511 - i
				b = i - 256
			else:
				r = i - 512
				g = 0
				b = 767 - i
			r -= j
			if r < 0:
				r = 0
			g -= j
			if g < 0:
				g = 0
			b -= j
			if b < 0:
				b = 0
			s += str(r) + " " + str(g) + " " + str(b) + " "
			i += 1
		i = 0
		j += 1
	while j < 512:
		while i < 768:
			if i < 256:
				r = 255 - i
				g = i
				b = 0
			elif i < 512:
				r = 0
				g = 511 - i
				b = i - 256
			else:
				r = i - 512
				g = 0
				b = 767 - i
			r -= 512 - j
			if r < 0:
				r = 0
			g -= 512 - j
			if g < 0:
				g = 0
			b -= 512 - j
			if b < 0:
				b = 0
			s += str(r) + " " + str(g) + " " + str(b) + " "
			i += 1
		i = 0
		j += 1
	return s

f = open("gradient.ppm", "w")
f.write(start() + gradient())
f.close()
