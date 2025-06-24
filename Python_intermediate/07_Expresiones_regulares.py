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

                                            # match

print("\n")

my_string = "Mi nombre es Angel Antonio, tengo 22 años y mi lenguaje favorito es Python."

match_result = re.match("Mi nombre es Angel", my_string) # Verifica si la cadena comienza con "Mi nombre es Angel", si al match le pasamos de la parte final de la cadena, no lo encontrara, ya que no es el inicio de la cadena.
print(match_result, "\n")

start, end = match_result.span() # Nos devuelve el inicio y el final del match
print(f"El match se encuentra en la posicion: {start, end}\n")

print(my_string[start:end]) # Imprime el texto que coincide con el match 

print("\n")

partner_description = "Mi pareja es Darli Mariela y es de la carrera de Educacion"
partner_match = re.match("Mi pareja es Darli Mariela", partner_description)

if partner_match is not None: # Si el match es encontrado, no sera None
    print(partner_match) # Imprime el objeto match
    longitud = partner_match.span() # Nos devuelve el inicio y el final del match
    print(f"El match se encuentra en la posicion: {longitud}\n")

                                    # Search

language_description = "Python es un lenguaje de programacion muy versatil y facil de aprender, me encanta python."

# Si queremos buscar un texto en cualquier parte de la cadena, usamos search
search_result = re.search("versatil", language_description) # Busca "versatil" en cualquier parte, no importa si es al inicio o al final de la cadena.
print(search_result, "\n")


                                        # Findall

# Si queremos encontrar todas las coincidencias de un texto en una cadena, usamos findall y me devuelve una lista con todas las coincidencias.

favorite_car = "Mi carro favorito es un Toyota Corolla, me encanta el COROLLA por su eficiencia y durabilidad."

# Aqui le colocamos el modificador re.I para que la busqueda no distinga entre mayusculas y minusculas.
search_findall = re.findall("Corolla", favorite_car, re.I) # Busca "Corolla" en cualquier parte de la cadena.

print(search_findall, "\n")

                                        # Split

# Si queremos dividir una cadena en partes, usamos split y nos devuelve una lista con las partes

favorite_house = "Mi casa favorita es una casa de campo: me encanta la casa de campo por su tranquilidad y belleza."

split_result = re.split(":", favorite_house) # Divide la cadena en partes usando la coma como separador.

print(split_result, "\n")

                                        # Sub 

# Si queremos reemplazar un texto en una cadena, usamos sub y nos devuelve la cadena con el texto reemplazado

favorite_color = "Mi color favorito es el azul, me encanta el color azul por su frescura y serenidad."

replace_result = re.sub("azul", "Blanco", favorite_color) # Reemplaza "azul" por "Blanco" en la cadena.

print(replace_result, "\n")

