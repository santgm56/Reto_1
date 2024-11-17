'''
Escribir una función que reciba una lista de string y retorne unicamente 
aquellos elementos que tengan los mismos caracteres. e.g. entrada: 
["amor", "roma", "perro"], salida ["amor", "roma"]
'''

def mismo_caracter(lista):
    resultado = []
    for palabra in lista:
        for otra_palabra in lista:
            '''
            Primero se compara si son diferentes indices y luego se comprueba 
            si tiene los mismos caracteres.
            '''
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                resultado.append(palabra)
    return resultado    

opcion = True
while opcion:
    lista = []
    maximo = int(input("¿Cuántas palabras desea ingresar en la lista? "))

    for i in range(maximo):
        palabra = input("Ingrese una palabra: ")
        lista.append(palabra)

    resultado = mismo_caracter(lista)
    print("La lista de palabras ingresada es:", lista)
    print("La lista de palabras que tienen los mismos caracteres es:", resultado)

    opcion = input("¿Desea comprobar otra lista de palabras? (s/n): ").lower()
    if opcion!= 's':
        opcion = False