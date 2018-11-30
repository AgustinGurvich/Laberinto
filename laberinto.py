def buscarSalida(laberinto,x,y,listapos):
    if laberinto[x][y]==1: #encontre una pared
        return False
    elif laberinto[x][y] == 2: #encontre la salida
        listapos.append((True,x,y))
        return listapos
    elif laberinto[x][y]==3: #encontre una ubicacion que ya visite
        return False
    laberinto[x][y]==3 #marco la ubicacion como visitada
    a = b = c = d = (False,x,y)
    if x < len(laberinto):
        a=buscarSalida(laberinto,x+1,y,listapos)
    if y < len(laberinto[0]):
        b=buscarSalida(laberinto,x,y+1,listapos)
    if  x > 0:
        c=buscarSalida(laberinto,x-1,y,listapos)
    if y > 0:
        d=buscarSalida(laberinto,x,y-1,listapos)
    if (a[0] or b[0] or c[0] or d[0]):
        return listapos.append((True,x,y))
    return False
def main():
    posiciones=[]
    labprueba=[[0,1,1,1],[0,1,1,1],[2,1,1,1]]
    buscarSalida(labprueba,0,0,posiciones)
main()
