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

import re

numero = "123-456-7890"
digito = r"\d{3}" # Busca 3 digitos seguidos
print(re.search(digito, numero))

print("\n")

area = int(input(" Introduce tu codigo de area del circulo a calcular: "))

calculo = (area ** 2) * 3.1416

print(f" El area del circulo es: {calculo}") 