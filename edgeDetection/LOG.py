import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os 

class filters():
    def __init__(self, image, sigma):
        self.sigma = sigma 
        self.n = image.size[0]
        self.image = image
        image = image.convert('L')
        self.imageMat = np.asarray(image.getdata()).reshape((self.n, self.n))

    def fftImage(self):
        return np.fft.fft2(self.imageMat)

    def gauss(self, x, y):
        return 1/(2*np.pi*self.sigma) * np.exp(-(x**2 + y**2)/(2*self.sigma))
    
    def fftLaplacian(self):
        mat = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                mat[i-int(self.n/2)][j-int(self.n/2)] = (i-self.n/2)**2 + (j-self.n/2)**2
        return mat

    def fftGaussian(self):
        mat = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                mat[i-int(self.n/2)][j-int(self.n/2)] = self.gauss(i-int(self.n/2), j-int(self.n/2))
        return mat 

    def gaussianFilter(self):
        return np.fft.ifft2(self.fftGaussian() * self.fftImage()).real

    def laplacianFilter(self):
        return np.fft.ifft2(self.fftLaplacian() * self.fftImage()).real

    def LOGFilter(self):
        return np.fft.ifft2(self.fftLaplacian() * self.fftImage() * self.fftGaussian()).real

    def thresholding(self):
        mat = self.LOGFilter()
        newMat = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                if mat[i][j] > 1: newMat[i][j] = 256
                else : newMat[i][j] = 0
        return newMat


    @staticmethod
    def gaussian(img, sigma):
        f = filters(img, sigma)
        return f.gaussianFilter()

    @staticmethod
    def laplacian(img):
        f = filters(img, sigma=1)
        return f.laplacianFilter()

    @staticmethod
    def LOG(img, sigma):
        f = filters(img, sigma)
        return f.LOGFilter()






        

def imageWork():
    mats = []
    for root, dirs, files in os.walk("."):
        for filenames in files:
            if filenames[:4] != 'gray':
                pass
            else:
                img = Image.open(root + '/' + filenames).convert('L')
                mats.append(np.asarray(img.getdata()).reshape((256, 256)))
    return mats[0]
            


