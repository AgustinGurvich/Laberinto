#include <string.h>
#include <stdio.h>

// crearlaberinto: int[][] int int int[][] int -> NONE
// crearlaberinto recibe una matriz bidimensional vacia, sus dimensiones de alto y ancho, una matriz con las direcciones
// de las paredes y su cantidad.
// Llena la matriz vacia con 1 si hay una pared en el lugar, 0 si no hay nada
void crearlaberinto(int laberinto[][],int alto,int ancho,int obstaculos[][],int cantobstaculos){
  int obstaculoact=0;
  for (int i=0; i<alto; i++){
    for(int j=0; j<ancho; j++){
      if (i==obstaculos[obstaculoact][i] && j==obstaculos[obstaculoact][j]){
        laberinto[i][j] = 0;
      }
      else{
        laberinto[i][j] = 0;
      }
      obstaculoact++;
    }
  }
}

// escribirlaberinto: int[][] int -> NONE
// escribirlaberinto recibe una matriz bidimensional de enteros y el numero maximo de submatrices que posee.
// Escribe en un archivo llamado "laberintogenerado.txt" todas las submatrices, linea por linea y les agrega un salto de linea
void escribirlaberinto(int laberinto[][],int alto){
  FILE *archivo;
  archivo = fopen("laberintogenerado.txt", "w+");
  for (int i=0; i<alto; i++){
    fprintf(archivo, "%d",laberinto[i]);
    fputs("\n",archivo);
  }
  fclose(archivo);
}

//main: NONE -> int
//Lee de un archivo llamado "parametrosLab.txt" los parametros necesarios para generar el laberinto, y luego de generarlo le agrega el objetivo 
//en la posicion indicada. Escribe la matriz resultante en el archivo indicado
int main(){
  FILE *archivo;
  int alto, ancho,finalx,finaly;
  archivo = fopen("parametrosLab.txt","r");
  fscanf(archivo, "%d %d", alto, ancho);
  fscanf(archivo, "%d %d", finalx,finaly);
  int obstaculos[alto*ancho][2];
  int cantobstaculos=0;
  while (fgetsc(archivo)!=EOF){
    fscanf(archivo, "%d %d", obstaculos[cantobstaculos][0],obstaculos[cantobstaculos][1]);
    cantobstaculos++;
  }
  fclose(archivo);
  int laberinto[alto][ancho];
  crearlaberinto(laberinto,alto,ancho,obstaculos,cantobstaculos);
  laberinto[finalx][finaly] = 2;
  escribirlaberinto(laberinto,alto);
  return 0;
}
