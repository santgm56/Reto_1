'''
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) 
entre dos números, según la elección del usuario, la forma de entrada de la función será 
los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
'''

def operaciones(x, y, operador): 
    '''
    Función que recibe dos números y una operación y devuelve el  resultado de la operación.
    '''
    if operador == "+":
        return x + y
    elif operador == "-": 
        return x - y
    elif operador == "*":
        return x * y
    elif operador == "/":
        while y == 0:
            print("No se puede dividir entre cero.")
            y = float(input("Ingrese un número para el denominador diferente de cero: "))
        return x / y
    else:
        return None

opcion = True
while opcion: # Ciclo que permite realizar varias operaciones.
    try: # Se intenta comprobar que los valores ingresados son números.
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Debe ingresar un número.")
        continue
    
    # Se pregunta al usuario qué operación quiere realizar.
    operacion = input("Ingrese la operación que deseas realizar (+, -, *, /): ")
    # Se llama a la función operaciones para obtener el resultado de la operación.
    resultado = operaciones(x, y, operacion) 
    if resultado is None: # Se comprueba que el tipo de operación sea válida.
        print("Operación no válida.")
        continue
    else:
        print(f"El resultado de la operación {x} {operacion} {y} es : {resultado}")

    # Se pregunta al usuario si desea realizar otra operación.
    opcion = input("¿Desea realizar otra operación? (s para Sí/ Cualquier otra tecla para No): ").lower() 
    if opcion != 's':
        opcion = False
