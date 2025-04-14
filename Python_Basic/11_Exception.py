
                                        ### Excepciones, Manejo de Errores. ###

# En Python, las excepciones son eventos que ocurren durante la ejecución de un programa y que indican un problema inesperado. Cuando un error o una circunstancia que no se espera ocurre, se lanza una excepción.

# La palabra clave "try" se utiliza para agrupar bloques de código que pueden generar excepciones.


print("\n")

""" Try with Except. """

num1 = 8
num2 = 3
#num2 = "3"

try:
    resultado = num1 / num2
    print(f"\nEl resultado de la division es: {round(resultado,2)}") # Aqui verifica si se cumple o no lo indicado

except:
    print("\nHubo un error en la division. Los valores deben ser numéricos.") # Solo se lanza si el programa no se cumple y da error.
    

print("\n")

""" Try with Except with Else wiht Finally. """

try:
    resultado = num1 + num2
    print(f"\nEl resultado de la suma es: {round(resultado,2)}")

except:
    print("\nHubo un error en la suma. Los valores deben ser numéricos.")
    
else: # Es opcional
    print("\nLa division se ha realizado correctamente.") # Se ejecuta sino se produce una excepcion...
    
finally: # Es opcional
    print("\nEl bloque finally se ejecuta siempre, independientemente de si hubo una excepción o no.\n") # El print da su definicion.
    
print("\n")

""" Excepciones for Type. """

valor1 = 9
valor2 = 5
valor2 = "5"

try:
    resultado = valor1 - valor2
    print(f"\nEl resultado de la resta es: {round(resultado,2)}")
    
except TypeError: # TypeError, es un tipo de error, aqui le estamos especificando que esta exception solo se lanzara si el error es de tipo TypeError...
    print("\nHubo un error en la resta. Los valores deben ser numéricos todos.")
    
print("\n")


# Captura de la excepcion de la informacion... 

try:
    resultado = valor1 - valor2
    print(f"\nEl resultado de la resta es: {round(resultado,2)}")
    
except ValueError as error: # Esta no se cumple
    print(error)
    
except Exception as err: # pero esta si se cumple y por eso se ejecuta el exception normal.
    print(err, "Hola, esto es un error, y se cumple ya que el anterior no lo hace. ") # Imprimo mi variable...
    
print("\n")

""" Excepciones para manejar errores por tipo. """

try:
    resultado = valor1 - valor2
    print(f"\nEl resultado de la resta es: {round(resultado,2)}")
    
except ValueError: # Aqui no se ejecutara la exception, porque le especificamos un tipo de error diferente al del problema.
    print("\nHubo un error en la resta. Los valores deben ser numéricos todos.")
    
print("\n")