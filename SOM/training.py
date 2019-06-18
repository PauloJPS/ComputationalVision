import os 
import numpy as np
import matplotlib.pyplot as plt
from som import *


def getImages():
    images = []
    for root, dirs, files  in os.walk(top='training/'):
        for f in files:
            fi = root + '/' + f
            images.append(fi)
    im = []
    for i in images:
        aux = plt.imread(i)
        im.append(aux)
    np.random.shuffle(im) 
    return im

def training(im, m, a, r, categories=10):
    cor = cortex(m, a, r, categories)
    aux = 0
    for i in im:
        aux += 1
        #if aux > 1000:break
        print(aux)
        cor.newImage(i)
    return cor

        
    
    

