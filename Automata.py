import numpy as np
import random
import matplotlib.pyplot as plt
import math as math
from celluloid import Camera
from toroidal.toroide import *
fig = plt.figure()
camera = Camera(fig)
class Automata():
    def __init__(self, dim):
        self.nuevaubicacion = []
        self.e1 = []
        self.e2 = []
        self.radio = []
        self.dim=dim-1
        self.theta = []
        self.a = np.zeros((dim, dim))
        self.a[0, 8] = 1
        self.a[14, 12] = 1
        self.a[2, 2] = 1
        self.a[3, 4] = 1
        self.a[4, 3] = 1
        self.a[10, 9] = 1
        self.a[2, 15] = 1
        self.a[14, 16] = 1
        self.a[18, 12] = 1
        self.a[6, 13] = 1
        self.a[0, 17] = 1
        self.a[13, 11] = 1
        self.a[9, 19] = 1
        self.a[4, 12] = 1
        self.a[7, 11] = 1
        self.a[4, 1] = 1
        self.a[15, 5] = 1
        self.a[18, 10] = 1
        self.a[18, 19] = 1
        self.a[16, 10] = 1

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
                self.indiceFuera(self.e1[i],self.e2[i],self.dim)

        self.nuevoconteo()
    def movimientoAutomata(self,ejex, ejey):
        self.n1 = random.randint(-1, 1)
        self.n2 = random.randint(-1, 1)
        self.nuevaubicacion.append((ejex+self.n1, ejey+self.n2))

    def indiceFuera(self,ejex,ejey,dim):

        if (ejex == 0 and ejey==0):  # es  decir  mi celda central es (0, 0)
            if(self.a[dim,dim] == 0 and self.a[0,dim] == 0 and self.a[1,dim] == 0 and self.a[dim,0] == 0 and
                    self.a[1,0] == 0 and self.a[dim,1] == 0 and self.a[0,1] == 0  and self.a[1,1] == 0 ):
                self.nuevaubicacion.append((movimientoAutomata_x0_y0(ejex,ejey,dim)))
                return ;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return;

        if (ejex == dim and ejey == dim):  # es  decir  mi celda central es (dim, dim)
            if (self.a[dim-1, dim-1] == 0 and self.a[dim, dim-1] == 0 and self.a[0, dim-1] == 0 and self.a[dim-1, dim] == 0 and
                    self.a[0, dim] == 0 and self.a[dim-1, 0] == 0 and self.a[dim, 0] == 0 and self.a[0, 0] == 0):
                self.nuevaubicacion.append((movimientoAutomata_xdim_ydim(ejex,ejey,dim)))
                return;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return;

        if (ejex == dim and ejey == 0):  # es  decir  mi celda central es (dim, 0)
            if (self.a[dim-1, dim] == 0 and self.a[dim, dim] == 0 and self.a[0, dim] == 0 and self.a[dim-1, 0] == 0 and
                    self.a[0, 0] == 0 and self.a[dim-1, 1] == 0 and self.a[dim, 1] == 0 and self.a[0, 1] == 0):
                self.nuevaubicacion.append((movimientoAutomata_xdim_y0(ejex,ejey,dim)))
                return;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return;

        if (ejex == 0 and ejey == dim):  # es  decir  mi celda central es (0, dim)
            if (self.a[dim, dim-1] == 0 and self.a[0, dim-1] == 0 and self.a[1, dim-1] == 0 and self.a[dim, dim] == 0 and
                    self.a[1, dim] == 0 and self.a[dim, 0] == 0 and self.a[0, 0] == 0 and self.a[1, 0] == 0):
                self.nuevaubicacion.append((movimientoAutomata_x0_ydim(ejex,ejey,dim)))
                return;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return;

        if(ejex==0):#es decir mi celda central es (0,y)
            if(self.a[dim,ejey+1]==0 and self.a[dim,ejey]==0 and self.a[dim,ejey-1]==0 and
            self.a[0,ejey+1]==0 and self.a[0,ejey-1]==0 and self.a[1,ejey+1]==0 and self.a[1,ejey]==0
            and self.a[1,ejey-1]==0 ):
                self.nuevaubicacion.append((movimientoAutomata_x0(ejex, ejey,dim)))
                return ;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return;

        if(ejex==dim): #es  decir  mi celda central es (dim, y)
            if (self.a[dim-1, ejey+1] == 0 and self.a[dim-1, ejey] == 0 and self.a[dim-1,ejey-1] == 0 and
                self.a[dim,ejey + 1] == 0 and self.a[dim,ejey - 1] == 0 and self.a[0,ejey + 1] == 0 and
                    self.a[0,ejey] == 0 and self.a[0,ejey- 1] == 0):
                self.nuevaubicacion.append(movimientoAutomata_xdim(ejex,ejey))
                return;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return;

        if(ejey==0):#es  decir  mi celda central es (x, 0)
            if(self.a[ejex-1,1]==0 and self.a[ejex-1,0]==0 and self.a[ejex-1,dim]==0 and
                self.a[ejex,1]==0 and self.a[ejex,dim]==0 and self.a[ejex+1,1]==0 and self.a[ejex+1,0]==0
                    and self.a[ejex+1,dim]==0):
                self.nuevaubicacion.append((movimientoAutomata_y0(ejex,ejey,dim)))
                return;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return ;

        if (ejey == dim): # es  decir  mi celda central es (x, dim)
            if (self.a[ejex - 1, 0] == 0 and self.a[ejex - 1, dim] == 0 and self.a[ejex - 1, dim-1] == 0 and
                    self.a[ejex, 0] == 0 and self.a[ejex, dim-1] == 0 and self.a[ejex + 1, 0] == 0 and self.a[ejex + 1, dim]==0
                    and self.a[ejex + 1, dim-1]==0 ):
                self.nuevaubicacion.append((movimientoAutomata_ydim(ejex,ejey)))
                return;
            else:
                self.nuevaubicacion.append((ejex,ejey))
                return ;

    #conciderar caso desborde de equinas
    #particulas de cualecensia juntar particulas y disminuir su velocidad de particulas
    #cada 4 se elimina y se ponen 4 al azar

    def nuevoconteo(self):
        self.a=np.zeros((dim,dim))
        self.radio = []
        self.theta = []
        for i in range(len(self.nuevaubicacion)):
            self.a[self.nuevaubicacion[i]] = 1
        self.nuevaubicacion=[]



#------------------------------
etapas = int(input("etapas: "))
dim=20
miAutomata = Automata(dim)
miAutomata.inicia(etapas)

#-------------------------
animation = camera.animate()
animation.save('celluloid_minimal.gif', writer = 'imagemagick')