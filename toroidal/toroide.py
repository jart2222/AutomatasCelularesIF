#aqui habra restricciones del movimiento toroidal
import random
def movimientoAutomata_xdim( ejex, ejey):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)
    if (n1==1):
        ejex=0
        ejey=n2+ejey
        return ejex,ejey;
    else:
        ejex=n1+ejex
        ejey=n2+ejey
        return ejex,ejey

def movimientoAutomata_x0( ejex, ejey,dim):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)
    if (n1==-1):
        ejex=dim
        ejey=n2+ejey
        return ejex,ejey;
    else:
        ejex=n1+ejex
        ejey=n2+ejey
        return ejex,ejey

def movimientoAutomata_ydim( ejex, ejey):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)
    if (n2==1):
        ejex=ejex+n1
        ejey=0
        return ejex,ejey;
    else:
        ejex=n1+ejex
        ejey=n2+ejey
        return ejex,ejey
def movimientoAutomata_y0( ejex, ejey,dim):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)
    if (n2==-1):
        ejex=ejex+n1
        ejey=dim
        return ejex,ejey;
    else:
        ejex=n1+ejex
        ejey=n2+ejey
        return ejex,ejey

def movimientoAutomata_x0_y0( ejex, ejey,dim):

    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)
    if (n1==-1 and n2==-1):
        ejex=dim
        ejey=dim
        return ejex,ejey;

    elif(n1==-1):
        ejex=dim
        ejey=n2+ejey
        return ejex,ejey;

    elif (n2 == -1):
        ejex = n1+ejex
        ejey = dim
        return ejex, ejey

    else:
        ejex = n1 + ejex
        ejey = n2 + ejey
        return ejex, ejey



def movimientoAutomata_xdim_ydim( ejex, ejey,dim):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)
    if (n1==1 and n2==1):
        ejex=0
        ejey=0
        return ejex,ejey;

    elif(n1==1):
        ejex=0
        ejey=n2+ejey
        return ejex,ejey;

    elif (n2 == 1):
        ejex = n1+ejex
        ejey = 0
        return ejex, ejey
    else:
        ejex = n1 + ejex
        ejey = n2 + ejey
        return ejex, ejey

def movimientoAutomata_xdim_y0( ejex, ejey,dim):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)

    if (n1<=0 and n2>=0):
        ejex = n1 + ejex
        ejey = n2 + ejey
        return ejex, ejey

    elif(n2==-1 and n1<=0):
        ejex = n1 + ejex
        ejey = dim
        return ejex, ejey

    elif (n1 == 1 and n2>= 0):
        ejex=0
        ejey=n2+ejey
        return ejex, ejey

    elif(n1==1 and n2==-1):
        ejex=0
        ejey=dim
        return ejex, ejey

def movimientoAutomata_x0_ydim( ejex, ejey,dim):
    n1 = random.randint(-1, 1)
    n2 = random.randint(-1, 1)

    if (n1 >= 0 and n2 <= 0):
        ejex = n1 + ejex
        ejey = n2 + ejey
        return ejex, ejey

    elif (n2 == 1 and n1 >= 0):
        ejex=ejex+n1
        ejey=0
        return ejex, ejey

    elif (n1 == -1 and n2 <= 0):
        ejex=dim
        ejey=ejey+n2
        return ejex, ejey

    elif (n1 == -1 and n2 == 1):
        ejex=dim
        ejey=0
        return ejex, ejey
