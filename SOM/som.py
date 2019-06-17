import numpy as np


class cortex:
    def __init__(self, m, a, r):
        self.__cortexS= 3*3*10 #cortex size
        self.__retinS = m #retin size
        self.__a = a #learning rate
        self.__r = r #genezalization radius

        self.initializeWeights()
        self.getCircle()

    def initializeWeights(self):
        self.Ws = np.random.rand(self.__cortexS, self.__cortexS, self.__retinS**2)

    def findNeuron(self):
        maxW = 0
        iW = 0
        jW = 0
        for i in range(self.__cortexS):
            for j in range(self.__cortexS):
                d = np.dot(self.Ws[i,j], self.im)
                if d > maxW:
                    maxW = d
                    iW = i
                    jW = j
        return iW, jW

    def updateWeights(self):
        iW, jW = self.findNeuron()
        delta = self.Ws[iW, jW] - self.im
        self.Ws[iW, jW] = self.Ws[iW, jW] - self.__a * delta
        for i in self.__circle:
            r = (i[0]**2 + i[1]**2)**0.5
            self.Ws[(i[0] + iW)%self.__cortexS, (i[1] + jW)%self.__cortexS] = (
                    self.Ws[(i[0] + iW)%self.__cortexS, (i[1] + jW)%self.__cortexS] -
                        self.__a * np.exp(-self.__r * r) * delta)

    def getCircle(self):
        x1 = [i for i in range(1, 1 + self.__r)]
        y1 = [int(np.sqrt(self.__r**2 - i**2)) for i in x1]
        y = []
        for i in range(len(x1)):
            y.append([(i,j)  for j in np.arange(1, 1 + y1[i])])
        
        c = [] 
        for i in y:
            c += i
        self.__circle = c

    def newImage(self, image):
        self.im = np.reshape(image, (self.__retinS**2, ))
        self.updateWeights()
    












