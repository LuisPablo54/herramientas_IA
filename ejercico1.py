#Ejercio 1
numero = int(input("Ingresa el número: "))
def sumatoria(numero):
    suma = 0
    total = 1
    
    while suma < numero:

        suma = suma + 1
        total = total * suma
        print(suma)

    print(f"Suma final: {total}")


sumatoria(numero)
print("Fin del programa")
