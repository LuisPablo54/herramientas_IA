#Ejericio 3
def palabras(palabra):
    palabra = list(palabra)
    nuevaPalabra = palabra.copy()
    nuevaPalabra.reverse()

    if palabra == nuevaPalabra:
        print("La palabra es igual")
    else:
        print("Son distintas")


palabra = input("Infrasa una palabra: ")
palabras(palabra)