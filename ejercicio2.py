#Ejercico 2
def sumatorio(numero):
    total = 0
    suma = 0
    
    while suma < numero:
        suma = suma + 1
        total = total + suma
        print(suma)
    print(f"Suma final: {total}")
    print("Fin del programa")

numero = int(input("Ingrsa el numero: "))
sumatorio(numero)