'''
Escribir una función que reciba una lista de números enteros y retorne 
la mayor suma entre dos elementos consecutivos.
'''

def maxima_suma_consecutivos(lista):
    max_suma = 0
    indice_1 = 0
    indice_2 = 1
    # Calcula la suma de cada par de elementos consecutivos y compara con la maxima suma.
    for i in range(len(lista) - 1):
        suma = lista[i] + lista[ i + 1]
        if suma > max_suma:
            max_suma = suma
            indice_1 = i
            indice_2 = i + 1
    return max_suma, indice_1, indice_2

opcion = True
while opcion:
    lista = []
    maximo = int(input("¿Cuántos números desea ingresar en la lista? "))

    # Ingresar los números en la lista
    for i in range(maximo):
        try:
            numero = int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un número entero.")
            continue
        lista.append(numero)

    # Mostrar la lista de números ingresada y la mayor suma entre dos elementos consecutivos.
    max_sum, indice_1, indice_2 = maxima_suma_consecutivos(lista)
    print("La lista de números ingresada es:", lista)
    print(f"La mayor suma entre dos elementos consecutivos, los cuales son: {lista[indice_1]} + {lista[indice_2]}  es: {max_sum}")
    
    opcion = input("¿Desea comprobar otra lista de números? (s/n): ").lower()
    if opcion!= 's':
        opcion = False

