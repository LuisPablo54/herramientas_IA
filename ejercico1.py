#Ejercicio 1

numero = int(input("Ingrsa el numero: "))

suma = 0
total = 1
def sumatoria (numero):
        
    while suma < numero:
    
        suma = suma + 1
        total = total * suma
        print(suma)

    print(f"Suma final: {total}")

print("Fin del programa")