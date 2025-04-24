### Challenge - Desafios ###

print("\n")

                                                    # EL FAMOSO "FIZZ BUZZ"
"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:

- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz". """

def numero():
    for index in range(1,101): # Creo un rango de 1 a 100.
        if index % 3 == 0 and index % 5 == 0: # Si el residuo de la division por 3 y 5 es 0, entonces es multiplo de 3 y 5.
            print("Fizzbuzz", "\n")
            
        elif index % 3 == 0: # Si el residuo de la division por 3 es 0, entonces es multiplo de 3.
            print("Fizz", "\n")
            
        elif index % 5 == 0: # Si el residuo de la division por 5 es 0, entonces es multiplo de 5.
            print("Buzz", "\n")
            
        else: # Si no es multiplo de 3 ni de 5, entonces imprime el numero.
            print(index, "\n")

numero() # Llamo a la funcion numero().

print("\n")


"""

                                                        Es un Anagrama?

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.

- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama. """

def anagrama (palabra1, palabra2): # Defino la funcion anagrama que recibe dos palabras.
    
    if palabra1.lower() == palabra2.lower():
        return " Estas palabras son iguales. "
    
    # Le pongo el metodo sorted() para que me ordene las letras de las palabras y las compare.
    # Le pongo el metodo lower() para que me convierta las letras a minusculas y las compare.
    elif sorted(palabra1.lower()) == sorted(palabra2.lower()): # Ordeno las letras de las palabras y comparo si son iguales.
        return " Estas palabras son anagramas. "
    
    else:
        return " Estas palabras no son anagramas. "
    
print(anagrama("roma", "Amor")) # Llamo a la funcion anagrama y le paso las palabras "roma" y "Amor".


print("\n")


                                                # LA SUCESIÓN DE FIBONACCI

"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    
    n = 50 # Limite de numeros a iterar.
    contador = 0 # Inicializo el contador en 0.
    first = 0 # Inicializo la variable a en 0.
    next = 1 # Inicializo la variable b en 1.
    
    while contador < n: # Hago un bucle while que se repite 50 veces.
        print(first, end=", ") # Imprimo el valor de a y le pongo una coma al final.

        total = first + next # Sumo a y b y lo guardo en la variable total.
        first = next 
        next = total
        contador += 1 # Incremento el contador en 1.

fibonacci() # Llamo a la funcion fibonacci().



print("\n")

# Otra forma de hacerlo es con una lista vacia y un for loop.
def Fibonacci():
    
    fib = [] # Inicializo una lista vacia.
    
    for i in range(0,50): # Hago un for loop de 0 a 50.
        
        if i == 0: # Si i es 0, entonces agrego 0 a la lista.
            fib.append(0) # Agrego 0 a la lista.
        elif i == 1: # Si i es 1, entonces agrego 1 a la lista.
            fib.append(1) # Agrego 1 a la lista.

        else: # Si i es mayor a 1, entonces agrego la suma de los dos anteriores a la lista.
            fib.append(fib[i-1] + fib[i-2]) # Agrego la suma de los dos anteriores a la lista.
        
    return fib # Retorno la lista.

print(Fibonacci())# Llamo a la funcion fibonacci().

print("\n")


# Otra Forma para la realizar la Sucesion de Fibonacci con el Bucle for.
def FIBONACCI():

    prev = 0 # Inicializo la variable a en 0.
    next = 1 # Inicializo la variable b en 1.

    for index in range(0,50):
        print(prev, end=", ") # Imprimo el valor de a y le pongo una coma al final.

        prev, next = next, prev + next
        
FIBONACCI() # Llamo a la funcion fibonacci().

print("\n")

