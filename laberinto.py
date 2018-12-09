# Representacion de datos:
# Usamos una lista de listas de caracteres para representar un laberinto
# Dicha matriz puede contener:
# "1": que representa una pared
# "2": que representa la salida
# "0": que representa un espacio en blanco
# "3": que representa una ubicacion ya visitada
#Usamos enteros para representar coordenadas, que son la posicion en el laberinto (int,int)
#Ejemplo: laberinto 5x5 con 5 obstaculos y salida en (3,4)
#   00000
#   10000
#   00010
#   11002
#   00010


#buscarSalida: list(list(char)) int int list() -> Bool
#buscarSalida recibe un laberinto, una coordenada x, una coordenada y, y una lista vacia
#Devuelve verdadero si se encontro la salida, falso en caso contrario
#Comienza buscando los casos base: Si encuentra una pared devuelve False, si enceuntra la salida devuelve True
#y si encuentra una ubicacion ya visitada devuelve False
#Si no sucede nada de eso, marca la ubicacion actual como visitada y comienza a buscar en otra casilla posible
#en este orden: abajo-derecha-izquierda-arriba
#Si encuentra la salida en alguna rama aniade la posicion actual (en forma de tupla) a la lista de posiciones
#y devuelve True
#Sino, busca en otra rama
#De no encontrar salida, devuelve False
def buscarSalida(laberinto,x,y,listapos):
    if laberinto[x][y]=="1": #encontre una pared
        return False
    elif laberinto[x][y]=="2": #encontre la salida
        listapos.append((x,y))
        return True
    elif laberinto[x][y]=="3": #encontre una ubicacion que ya visite
        return False
    laberinto[x][y]="3" #marco la ubicacion como visitada
    if x < len(laberinto)-1:
        if (buscarSalida(laberinto,x+1,y,listapos)):
            listapos.append((x,y))
            return True
    if y < len(laberinto[x])-2: #tomo en cuenta el caracter '\n'
        if (buscarSalida(laberinto,x,y+1,listapos)):
            listapos.append((x,y))
            return True
    if  x > 0:
        if (buscarSalida(laberinto,x-1,y,listapos)):
            listapos.append((x,y))
            return True
    if y > 0:
        if (buscarSalida(laberinto,x,y-1,listapos)):
            listapos.append((x,y))
            return True
    return False

def test_buscarSalida():
    assert buscarSalida([["0","0","1"],["2","1","0"],["1","1","0"]],1,0,[])==True
    assert buscarSalida([["0","0","1"],["2","1","0"],["1","1","0"]],0,2,[])==False
    assert buscarSalida([["0","0","1"],["0","0","2"],["3","1","0"]],1,0,[])==False
    assert buscarSalida([["1","1","1"],["1","0","1"],["1","1","1"]],1,1,[])==False

#main: NONE -> NONE
#main lee un laberinto desde el archivo "laberintogenerado.txt" y lo guarda en una lista
#Luego separa los caracteres de cada string en sublistas
#Llama a buscarSalida para revisar si existe una salida
#Si la lista de posiciones es vacia, avisa que no existe salida
#Caso contrario, imprime la lista de posiciones a seguir para encontrar la salida
def main():
    laberinto=[]
    archivo=open("laberintogenerado.txt","r")
    laberinto = archivo.readlines()
    archivo.close()
    for i in range(len(laberinto)):
        # laberinto[i]=laberinto[i][0:100]
        laberinto[i]=list(laberinto[i])
    posiciones=[]
    resolucion = buscarSalida(laberinto,0,0,posiciones)
    posiciones.reverse()
    if (len(posiciones)==0):
        print("No se pudo encontrar el camino hacia el objetivo")
    else:
        print("Posiciones a seguir para resolver el laberinto:\n" + str(posiciones))
main()
