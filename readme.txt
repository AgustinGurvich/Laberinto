El programa para generar el laberinto se encuentra en el archivo "generador.c"
Asumimos que las coordenadas a colocar coinciden con las de una matriz (desde el 0 hasta el (tamaño de la matriz)-1 )
El archivo de entrada que recibe el generador se llama "parametrosLab.txt", el cual tiene la siguiente forma:
Linea 1: alto y ancho del laberinto, separados por un espacio
Linea 2: ubicacion de la salida (coordenadas x e y, separadas por un espacio)
Linea 3: cantidad de paredes a colocar
En el resto de las lineas hasta el fin del archivo se colocan (linea por linea) las coordenadas de las paredes (x e y), separadas por un espacio.
Se asume que el inicio se encuentra en la coordenada (0,0), por lo cual no se espera que se coloque un obstaculo alli.
Luego, el laberinto generado se guarda en el archivo "laberintogenerado.txt", en el cual cada linea
es una fila del laberinto, donde todas tienen un caracter \n al final de la linea.
Se adjunta un archivo de muestra, que genera un laberinto de tamaño 6x7 con salida en la coordenada (4,6) y 7 obstaculos en las posiciones
(0,1),(0,5),(4,0),(4,1),(4,2),(4,3),(5,5)
