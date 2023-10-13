#Ejericio 3

palabra = input("Infrasa una palabra: ")
palabra = list(palabra)
nuevaPalabra = palabra.copy()
nuevaPalabra.reverse()

if palabra == nuevaPalabra:
    print("La palabra es igual")
else:
    print("Son distintas")