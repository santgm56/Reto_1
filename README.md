# Programación Orientada a Objetos - Reto 1

## Estudiante: Santiago Gamboa Martínez

Como llegué a la solución de cada uno de los puntos del reto:

1.  **Función de Operaciones Básicas:** Necesitaba implementar una función que realizara operaciones básicas. Para esto hice lo siguiente:

    - Diseñé una función que el usuario indicara como entrada los dos operandos y el operador, para que la función pueda devolver el resultado correspondiente.

    - Me dí cuenta que las divisiones por 0 pueden resultar en un error. Por lo tanto, implementé un manejo especial con un bucle `while` para que el programa le pida al usuario que digite un número diferente a 0 como denominador.

    - Estructuré dos variables que contienen el valor de la entrada del usuario de los dos números. Me di cuenta que si el usuario digitaba un valor diferente a un número, podía presentar errores. Para esto, implementé un `try-except` que valida la entrada de valores correctos. De la misma forma, hice que en la variable que contiene la entrada del tipo de operación tuviera un manejo especial, en el caso que el usuario digitara un valor diferente a una operación. En última instancia, el programa retorna el resultado y lo imprime.

2.  **Función de validación de palíndromos:** Necesitaba implementar una función que validara si una palabra es un palíndromo, sin usar la técnica del slicing: Para esto hice lo siguiente:

    - Como condición de NO usar **slicing**, pude identificar que puedo diseñar una función que utiliza un bucle `for`. Para esto, primero, eliminé los espacios y convertí la palabra a minúsculas. Luego, utilicé el bucle `for` para recorrer la palabra desde el primer al último carácter. Me dí cuenta que en cada iteración puedo comparar el carácter en la posición **_i_** con su correspondiente en la posición contraria, que es **_[-i-1]_**, lo cual me permite identifica si la palabra es un palíndromo. Por ejemplo, si la palabra es "perro", que tiene 5 caracteres, accede al primer carácter en la posición **i = 0**, que es la "p", y comparo este con el carácter en la posición contraria **_[-i-1]_**, que sería el índice -1, es decir, la "o".

    - Implementé una condición `if`, para que el resultado se imprima de acuerdo al resultado retornado de la función.

3.  **Función que valida números primos en una lista:**
    Necesitaba implementar una función que retornara los números primos de una lista. Para esto hice los siguiente:

    - Implementé un primer bucle `for` que reccorre todos los elementos de una lista. Como el número 1 no es un número primero, creé una condición `if` que procesa números mayores a 1. También, me di cuenta que un número primo solo tiene el el 1 y el mismo como divisores. Por lo tanto, implementé un segundo bucle `for` que recorre un rango de números desde el 2 hasta el número - 1, ya que el rango no toma el valor del final, verificando si el número es divisible por algunos de estos números en el rango. También añadí un `break` que interrumpe el ciclo en el caso que el número no sea primo, si no es así, usé un else que añade el número a lista de números primos.

    - Para la entrada del usuario, con un `input()` le solicita al usuario cuantos números quiere ingresar a la lista. Luego, con un bucle `for`, el programa le pide al usuario ingresar los números. Como la condición es que sean solo enteros, creé un manejo errores `try-except`, que hace si el usuario ingresa un número no entero, le muestra un mensaje de error y le permite intentarlo de nuevo. Luego, el programa para que la lista imprima la lista de primos de manera ordenada utilicé el método `.sort()`</li>

4.  **Función que suma los dos números mayores consecutivos:** Necesitaba implementar una función que toamara una lista de números e identificara los dos números mayores consecutivos para que los sume. Para esto hice lo siguiente:

    - Primero, inicié tres variables que puedan almacenar la suma máxima y los índices de los elementos que la generan. Luego de esto, puede ver que con un bucle for puedo recorre toda la lista, sumando cada par de elementos consecutivos y comparando la suma con la máxima encontrada hasta ese momento. En el caso en que la suma fuera mayor, actualiza la variable de la suma máxima y los índices correspondientes. Me di cuenta de que para evitar que el bucle intentara acceder a un índice fuera del rango de la lista, debía restarle 1 al valor de la longitud de la lista, de modo que el bucle solo recorriera hasta el penúltimo elemento.

    - Como en el punto 3, con un input() le solicita al usuario cuantos números quiere ingresar a la lista. Luego, con un bucle for, el programa le pide al usuario ingresar los números y con un try-except valida si estos números ingresados son enteros. </

5.  **Función que valida que dos elementos tenga los mismos carácteres:**
    Necesitaba crear una función que reciba una lista de string para que retorne los elementos que tengan los mismos caracteres.

    - He implementado un bucle `for` que recorre todos los elementos de la lista. Luego, dentro de este bucle `for`, un segundo bucle for recorre nuevamente todos los elementos de la lista, pero solo compara las palabras que tiene indice diferente. Para que la misma palabra no se compare, uso una condición `if`. Además, en el `if` añadí la condición para que se puedan comparar dos palabras diferentes que no importe el orden de los carácteres, esto pude solucionarlo con el método `.sorted()` para que ordene los carácteres de cada palabra alfabéticamente. Si las dos condiciones del `if` se cumplen, las palabras se incluyen en la lista de resultado.

    - Un poco similar al punto 3 y 4, con un `input()` le solicita al usuario cuantas palabras quiere ingresar a la lista. Luego, con un bucle for, el programa le pide al usuario las palabras que desee. Por último, el programa con un print imprime la lista "resultado" que es retornada por la función.

**PD: En cada uno de los puntos, como forma de mejorar la funcionalidad del programa, implementé un manejo especial con un bucle while para que el usuario pudiera usar el programa tanta veces desee.**
