'''
Escribir una función que reciba una lista de números y devuelva solo aquellos 
que son primos. La función debe recibir una lista de enteros y retornar solo 
aquellos que sean primos.
'''

def es_primo(lista):
    primos = []
    for numero in lista:
        if numero > 1:
            '''
            Comprobar si el número es primo verificando que no sea divisible por 
            ningún número entre 2 y el número - 1.
            '''
            for i in range(2, numero):
                if (numero % i) == 0:
                    break
            else:
                primos.append(numero)
    return primos

opcion = True
while opcion:
    lista = []
    maximo = int(input("¿Cuántos números desea ingresar en la lista? "))
    for i in range(maximo):
        try:
            numero = int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un número entero.")
            continue
        lista.append(numero)
    
    primos = es_primo(lista)
    primos.sort()
    print(f"Los números primos de la lista son: {primos}")

    opcion = input("¿Desea comprobar otra lista de números? (s/n): ").lower()
    if opcion != 's':
        opcion = False