def buscarSalida(laberinto,x,y,listapos):
    print(x,y)
    if laberinto[x][y]==1:
        return (False,x)
    elif laberinto[x][y] == 2:
        listapos.append((x,y))
        tupla = True
        return tupla
    elif laberinto[x][y]==3: #encontre una ubicacion que ya visite
        return False
    laberinto[x][y]=3 #marco la ubicacion como visitada
    a=b=c=d=False
    if x < len(laberinto)-1:
        a = buscarSalida(laberinto,x+1,y,listapos)
    if y < len(laberinto[x])-1:
        b = buscarSalida(laberinto,x,y+1,listapos)
    if  x > 0:
        c = buscarSalida(laberinto,x-1,y,listapos)
    if y > 0:
        d = buscarSalida(laberinto,x,y-1,listapos)
    if (a or b or c or d):
        listapos.append((x,y))
        tupla = True
        return tupla
    return False
def main():
    posiciones=[]
    labprueba=[[0,1,1,1],[0,0,1,1],[1,0,0,2]]
    resolucion = buscarSalida(labprueba,0,0,posiciones)
    print(posiciones)
main()
