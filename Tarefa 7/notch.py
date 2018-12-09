import numpy, math
from PIL import Image

I = Image.open('lula.jpg')
I = I.convert('L')

def notch(img, x, y, r):
	for i in range(-r, r+1):
		for j in range(-r, r+1):
			u = x+i
			v = y+j
			Duv = math.sqrt(i*i+j*j)
			D0 = 30.0
			#ordem do filtro
			n = 2
			Huv = 1.0/(1+((D0/(Duv+0.001))**(2*n)))
			if u < 0 or v < 0:
				continue
			if u >= I.size[0] or v >= I.size[1]:
				continue
			img[v][u] = Huv*img[v][u]

a = numpy.asarray(I)
A = numpy.fft.fft2(a)
A = numpy.fft.fftshift(A)

#apagando duas regioes retangulares
notch(A, 863, 538, 50)
notch(A, 737, 663, 50)

notch(A, 137, 663, 50)
notch(A, 63, 537, 50)
notch(A, 264, 537, 50)
notch(A, 1337, 663, 50)
notch(A, 1463, 537, 50)
notch(A, 1538, 663, 50)
notch(A, 737, 1113, 50)
notch(A, 722, 1161, 50)
notch(A, 863, 1138, 50)

notch(A, 720, 711, 50)
notch(A, 877, 490, 50)

Image.fromarray(abs(A)/800).show()

#lembre-se de descentralizar antes de aplicar a inversa
A = numpy.fft.fftshift(A)

output = Image.fromarray(numpy.fft.ifft2(A).astype(numpy.uint8))
output.show()

