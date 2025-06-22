# expresiones regulares 

"""/hola/ texto especifico a encontrar
\d cualquier digito
\D cualquier no digito
\w un caracter de palabra como una letra
. cualquier caracter
+ una o mas veces del caracter anterior
* cero o mas veces del caracter anterior
? cero o una vez del caracter anterior


"""
print("\n")

import re

numero = "123-456-7890"
digito = r"\d{4}" # Busca 4 digitos seguidos
print(re.search(digito, numero))

print("\n")

my_string = "Mi nombre es Angel Antonio, tengo 22 años y mi lenguaje favorito es Python."

match_result = re.match("Mi nombre es Angel", my_string) # Verifica si la cadena comienza con "Mi nombre es Angel", si al match le pasamos de la parte final de la cadena, no lo encontrara, ya que no es el inicio de la cadena.
print(match_result, "\n")

start, end = match_result.span() # Nos devuelve el inicio y el final del match
print(f"El match se encuentra en la posicion: {start, end}\n")

print(my_string[start:end]) # Imprime el texto que coincide con el match    

# Si queremos buscar un texto en cualquier parte de la cadena, usamos search
search_result = re.search("Python", my_string) # Busca "Python" en cualquier parte, no importa si es al inicio o al final de la cadena.



print("\n")
# area = int(input(" Introduce tu codigo de area del circulo a calcular: "))

# calculo = (area ** 2) * 3.1416

# print(f" El area del circulo es: {calculo}") 