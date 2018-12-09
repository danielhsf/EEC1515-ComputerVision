#include <stdio.h>
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace cv;

int main(int argc, char** argv) {

	//o primeiro argumento da linha de comando é a imagem na qual será feito o template matching
	Mat img1 = imread(argv[1], CV_LOAD_IMAGE_GRAYSCALE);
	//o segundo argumento da linha de comando é a imagem de referência para o template matching
	Mat temp = imread(argv[2], CV_LOAD_IMAGE_GRAYSCALE);
	//img2: onde será armazenado o resultado
	Mat img2(img1.size(), img1.type());

	//variável para indicar se o thresholding será aplicado
	int aplicarThreshold = 0;
	if(argc <= 3)
		aplicarThreshold = 0;
	else
		aplicarThreshold = atoi(argv[3]);
	int threshold;
	if(aplicarThreshold)
		threshold = atoi(argv[4]);

	//armazena a soma das diferenças ao quadrado (SSD) para cada pixel
	Mat imgSSD(img1.size(), CV_32F);

	//m representa metade do tamanho do template (largura)
	//n representa metade do tamanho do template (altura)
	int m = temp.cols/2;
	int n = temp.rows/2;

	//maior valor SSD para propósitos de normalização
	int maiorValor = 0;

	//(i, j) percorre a imagem
	for(int i = n; i < img1.rows - n; i++) {
		for(int j = m; j < img1.cols - m; j++) {
			//SSD = sum of squared differences
			int sum = 0;
			//(s, t) percorre o template
			for(int s = -n; s <= n; s++) {
				for(int t = -m; t <= m; t++) {
					int dif = (int) temp.at<uchar>(s+n, t+m) - (int) img1.at<uchar>(i+s, j+t);
					sum += dif*dif;
				}
			}
			imgSSD.at<float>(i, j) = sum;
			if(sum > maiorValor)
				maiorValor = sum;
		}
	}

	//normalização
	for(int i = n; i < img1.rows - n; i++) {
		for(int j = m; j < img1.cols - m; j++) {
			int v = 255-255*(imgSSD.at<float>(i, j)/maiorValor);
			//limiar (thresholding)
			img2.at<uchar>(i, j) = v;
			if(aplicarThreshold) {
				if(v > threshold)
					img2.at<uchar>(i, j) = 255;
				else
					img2.at<uchar>(i, j) = 0;
			}
		}
	}
	

	//cria uma janela denominada "original"
	namedWindow("original", 1);
	//exibe img1 na janela "original"
	imshow("original", img1);
	//cria uma janela denominada "resultado"
	namedWindow("resultado", 1);
	//exibe img2 na janela "resultado"
	imshow("resultado", img2);

	//espera que o usuário aperte alguma tecla para finalizar o programa
	waitKey(0);

	return 0;
}
