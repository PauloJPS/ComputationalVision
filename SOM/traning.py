import os 
from som import *


def getImages():
    images = []
    for root, dirs, files  in os.walk(top='testing/'):
        for f in files:
            fi = root + '/' + f
            images.append(fi)
    return images
     
def training(im):
    pass
    

