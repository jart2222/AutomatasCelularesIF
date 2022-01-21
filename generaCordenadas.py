import random

def movimientoAutomata():
    n1 = random.randint(0, 19)
    n2 = random.randint(0, 19)
    return f'{n1},{n2}'

for i in range(20):
    print(f'self.a[{movimientoAutomata()}]=1')