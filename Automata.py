import numpy as np
import random
import matplotlib.pyplot as plt
import math as math
from celluloid import Camera
fig = plt.figure()
camera = Camera(fig)
class Automata():
    def __init__(self, dim):
        self.nuevaubicacion = []
        self.e1 = []
        self.e2 = []
        self.radio = []
        self.theta = []
        self.a = np.zeros((dim, dim))
        self.a[1, 0] = 1
        self.a[8, 2] = 1
        self.a[4, 4] = 1
        self.a[14, 3] = 1
        self.a[10, 7] = 1
        self.a[5, 7] = 1
        self.a[4, 2] = 1
        self.a[11, 14] = 1
        self.a[15, 7] = 1
        self.a[15, 13] = 1

    def inicia(self,etapas):
        for etapa in range(etapas):
                self.inspeccionMatrice()
                self.checharVecindades()
                self.inspeccionMatrice()

    def inspeccionMatrice(self):
        self.e1=[]
        self.e2=[]
        for index, x in np.ndenumerate(self.a):
            if (x == 1):
                self.centrarGrafica(index[0],index[1])
                self.e1.append(index[0])
                self.e2.append(index[1])


        plt.polar(self.theta, self.radio, 'go')
        camera.snap()
    def centrarGrafica(self, ejex, ejey):
        self.convertirToPolares(ejex - dim / 2, ejey - dim / 2)

    def convertirToPolares(self, ejex, ejey):
        self.radio.append(math.sqrt((ejex) ** 2 + ejey ** 2))
        if ejex== 0:
            self.theta.append(1.5708)
        else:
            self.theta.append(math.atan2(ejey,ejex))

    def checharVecindades(self):
        for i in range(len(self.e1)):
            try:
                if (self.a[self.e1[i] - 1, self.e2[i]] == 0 and self.a[self.e1[i] + 1, self.e2[i]] == 0 and
                        self.a[self.e1[i], self.e2[i] - 1] == 0 and self.a[self.e1[i], self.e2[i] + 1] == 0 and
                        self.a[self.e1[i] - 1, self.e2[i] - 1] == 0 and self.a[self.e1[i] - 1, self.e2[i] + 1] == 0 and
                        self.a[self.e1[i] + 1, self.e2[i] - 1] == 0 and self.a[self.e1[i] + 1, self.e2[i] + 1] == 0):

                    self.movimientoAutomata(self.e1[i],self.e2[i])
                else:
                    self.nuevaubicacion.append((self.e1[i], self.e2[i]))

            except IndexError:
                self.indiceFuera(self.e1[i],self.e2[i])

        self.nuevoconteo()
    def indiceFuera(self,ejex,ejey):
        if (ejex == 0):
            self.nuevaubicacion.append((dim-1,ejey))

        if (ejex == dim - 1):
            self.nuevaubicacion.append((0,ejey))

        if (ejey == 0):
            self.nuevaubicacion.append((ejex,dim-1))

        if (ejey== dim - 1):
            self.nuevaubicacion.append((ejex,0))


    def movimientoAutomata(self,ejex, ejey):
        self.n1 = random.randint(-1, 1)
        self.n2 = random.randint(-1, 1)
        self.nuevaubicacion.append((ejex+self.n1, ejey+self.n2))

    def nuevoconteo(self):
        self.a=np.zeros((dim,dim))
        self.radio = []
        self.theta = []
        for i in range(len(self.nuevaubicacion)):
            self.a[self.nuevaubicacion[i]] = 1

        self.nuevaubicacion=[]




etapas = int(input("etapas: "))


#-------------------------
dim=20;
miAutomata = Automata(dim);
miAutomata.inicia(etapas)

#-------------------------
animation = camera.animate()
animation.save('celluloid_minimal.gif', writer = 'imagemagick')

