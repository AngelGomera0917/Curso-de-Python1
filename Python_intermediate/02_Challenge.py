### Challenge - Desafios ###

print("\n")

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
        return False
    else:
        return True
    
print(anagrama("roma", "Amor"))





