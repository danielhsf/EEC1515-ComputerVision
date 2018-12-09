import Image, numpy, math
I = Image.open('img2.jpg')
I = I.convert('L')
a = numpy.asarray(I)
A = numpy.fft.fft2(a)
A = numpy.fft.fftshift(A)

for u in range(I.size[0]):
	for v in range(I.size[1]):
		u1 = u - I.size[0]/2
		v1 = v - I.size[1]/2
		Duv = math.sqrt(u1*u1 + v1*v1)
		#ordem do filtro
		n = 5
		#limiar
		D0 = 600
		Huv = 1.0/((1+Duv/D0)**(2*n))
		A[v][u] = Huv*A[v][u]

Image.fromarray(abs(A)/800).show()
A = numpy.fft.fftshift(A)

output = Image.fromarray(numpy.fft.ifft2(A).astype(numpy.uint8))
output.show()

