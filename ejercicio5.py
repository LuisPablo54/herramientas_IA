#Ejercicio 5
def listas(tamano,indice):
    miLista = [numero for numero in range(0, tamano + 1)]
    print(miLista)

    vector = []



    for i in range(0, tamano + 1):
        if i == indice:
            continue
        else:
            vector.append(i)
        


    print(vector)

tamano = int(input("El tamaño del vector: ")) #Determian el tamañano de la lista
indice = int(input("El indice es: "))

listas(tamano, indice)
