# Declarar librería para el uso de numeros aleatorios
import random

# Se define el tamaño de filas y columnas
filas, columnas=2,2

# Se declara las matrices
A1=[]
A2=[]
producto=[]


# Se crea la matriz 1

for i in range(filas):
    col1=[]
    for j in range(columnas):
        col1.append(random.randint(0,10))
    A1.append(col1)  
print("La matriz 1:")      
print(A1)

# Se crea la matriz 2

for i in range(filas):
    col2=[]
    for j in range(columnas):
        col2.append(random.randint(0,10))
    A2.append(col2)
print("La matriz 2:")
print(A2)

# Se declara la  función para multiplicar


def multiplicarmatriz ():
    for i in range(filas):
        producto.append([0]*columnas)
        for j in range(columnas):
            producto[i][j]=A1[i][j]*A2[i][j]
    print("La matriz producto es:")
    print(producto)     

# Se llama a la función
multiplicarmatriz()   