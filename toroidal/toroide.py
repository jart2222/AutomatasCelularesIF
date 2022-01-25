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
