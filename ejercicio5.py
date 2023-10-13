#Ejercicio 5
tamaño = int(input("El tamaño del vector: ")) #Determian el tamañano de la lista
indice = int(input("El indice es: "))

miLista = [numero for numero in range(0, tamaño + 1)]
print(miLista)

vector = []



for i in range(0, tamaño + 1):
    if i == indice:
        continue
    else:
        vector.append(i)
    


print(vector)


