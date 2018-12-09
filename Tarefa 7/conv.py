import numpy
from PIL import Image
I = Image.open('lula.jpg')
I = I.convert('L')
a = numpy.asarray(I)

filtro = numpy.zeros(a.shape)
a.flags.writeable = True
filtro.flags.writeable = True

#filtro da media tamanho M por M
M = 20
for i in range(M):
	for j in range(M):
		filtro[i][j] = 1.0/(M*M)

S = numpy.fft.fft2(filtro)
A = numpy.fft.fft2(a)

print(S)
print(A)

#no dominio da frequencia o produto corresponde a convolucao no dominio espacial
res = numpy.multiply(S, A)

S = numpy.fft.fftshift(S)
A = numpy.fft.fftshift(A)
#exibindo o filtro e a imagem no dominio da frequencia
#observe que os espectros sao multiplicados por fatores diferentes para fins de visualizacao
Image.fromarray(abs(S*200).astype(numpy.uint8)).show()
Image.fromarray(abs(A/400).astype(numpy.uint8)).show()

Image.fromarray(numpy.fft.ifft2(res).astype(numpy.uint8)).show()
I.show()
