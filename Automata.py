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
        self.a[124, 431] = 1
        self.a[278, 806] = 1
        self.a[469, 326] = 1
        self.a[617, 734] = 1
        self.a[283, 430] = 1
        self.a[204, 928] = 1
        self.a[540, 645] = 1
        self.a[123, 172] = 1
        self.a[430, 239] = 1
        self.a[510, 661] = 1
        self.a[990, 317] = 1
        self.a[305, 825] = 1
        self.a[903, 16] = 1
        self.a[731, 366] = 1
        self.a[78, 607] = 1
        self.a[333, 479] = 1
        self.a[240, 264] = 1
        self.a[55, 394] = 1
        self.a[832, 839] = 1
        self.a[941, 638] = 1
        self.a[996, 758] = 1
        self.a[982, 320] = 1
        self.a[302, 326] = 1
        self.a[966, 650] = 1
        self.a[634, 251] = 1
        self.a[954, 318] = 1
        self.a[782, 278] = 1
        self.a[551, 196] = 1
        self.a[120, 921] = 1
        self.a[980, 969] = 1

    def inicia(self,etapas):
        for etapa in range(etapas):
                self.inspeccionMatrice()
                self.checharVecindades()
                self.inspeccionMatrice()

    def inspeccionMatrice(self):
        for index, x in np.ndenumerate(self.a):
            if (x == 1):
                self.centrarGrafica(index[0], index[1])
                self.e1.append(index[0])
                self.e2.append(index[1])
            else:
                pass
        plt.polar(self.theta, self.radio, 'go')
        camera.snap()

    def centrarGrafica(self, ejex, ejey):
        self.ConvertirToPolares(ejex - dim / 2, ejey - dim / 2)

    def ConvertirToPolares(self, ejex, ejey):
        self.radio.append(math.sqrt((ejex) ** 2 + ejey ** 2))
        if ejex== 0:
            self.theta.append(1.5708)
        else:
            self.theta.append(math.atan2(ejey,ejex))

    def checharVecindades(self):
        for i in range(len(self.e1)):
            if (self.a[self.e1[i] - 1, self.e2[i]] == 0 and self.a[self.e1[i] + 1, self.e2[i]] == 0 and
                    self.a[self.e1[i], self.e2[i] - 1] == 0 and self.a[self.e1[i], self.e2[i] + 1] == 0 and
                    self.a[self.e1[i] - 1, self.e2[i] - 1] == 0 and self.a[self.e1[i] - 1, self.e2[i] + 1] == 0 and
                    self.a[self.e1[i] + 1, self.e2[i] - 1] == 0 and self.a[self.e1[i] + 1, self.e2[i] + 1] == 0):

                self.movimientoAutomata(self.e1[i],self.e2[i])

            else:

                self.nuevaubicacion.append((self.e1[i], self.e2[i]))

        self.nuevoconteo()

    def movimientoAutomata(self,ejex, ejey):
        self.n1 = random.randint(-1, 1)
        self.n2 = random.randint(-1, 1)
        self.nuevaubicacion.append((ejex+self.n1, ejey+self.n2))

    def nuevoconteo(self):
        self.e1 = []
        self.e2 = []
        self.a = np.zeros((dim, dim))
        self.radio = []
        self.theta = []
        for i in range(len(self.nuevaubicacion)):
            self.a[self.nuevaubicacion[i]] = 1
        self.nuevaubicacion = []



etapas = int(input("etapas: "))


#-------------------------
dim=1000
miAutomata = Automata(dim);
miAutomata.inicia(etapas)

#-------------------------
animation = camera.animate()
animation.save('celluloid_minimal.gif')

