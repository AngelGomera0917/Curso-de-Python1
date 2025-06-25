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

                                        # Patterns

# Podemos crear patrones mas complejos usando expresiones regulares

favorite_career = "Mi sueño es poder ser un Deasarrollador de Software FullStack, y Poder aprender DepVops en 3 o 4 años."

# Le colocamos el [Mm] para que busque tanto "Mi" como "mi". 
patterns_match = r"[Mm]i sueño es ser un Deasarrollador de Software"
print(re.match(patterns_match, favorite_career))

print("\n")

patterns_search = r"FullStack"
print(re.search(patterns_search, favorite_career))

print("\n")

patterns_findall = r"[Pp]oder"
print(re.findall(patterns_findall, favorite_career)) # Busca "poder" o "Poder" en la cadena.

print("\n")

patterns_findall = r"\d" # \d cualquier digito, busca cualquier numero dentro de la cadena de texto.
print(re.findall(patterns_findall, favorite_career)) 

print("\n")

patterns_findall = r"[0-9]" # [0-9] Me busca todos los numeros dentro de la cadena que sean de 0 al 9
print(re.findall(patterns_findall, favorite_career)) 

print("\n")

patterns_split = r","
print(re.split(patterns_split, favorite_career))

print("\n")

patterns_sub = r"aprender"
print(re.sub(patterns_sub, "ser un master en", favorite_career))

print("\n")

# valid_email_pattern: Expresión regular para validar correos electrónicos.
# ^: Inicio de la cadena.
# [a-zA-Z0-9._%+-]+: Parte local del correo (antes del @), permite letras, números y ciertos caracteres especiales.
# @: Símbolo obligatorio que separa la parte local del dominio.
# [a-zA-Z0-9]+: Parte del dominio (después del @), permite letras y números.
# \.: Punto que separa el nombre del dominio de la extensión.
# [a-zA-Z0-9]+: Extensión del dominio (por ejemplo, com, org, net), permite letras y números.
# $: Final de la cadena.

# Validar si un correo electonico es valido


user_gmail = "antoniogomera09@gmail.com"

# El signo $ indica el final de la cadena, y el signo ^ indica el inicio de la cadena.
valid_email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"

if re.match(valid_email_pattern, user_gmail): #
    print(f"El correo {user_gmail} es valido.\n")

if re.search(valid_email_pattern, user_gmail): 
    print(f"El correo {user_gmail} es valido.\n")

if re.findall(valid_email_pattern, user_gmail):
    print(f"El correo {user_gmail} es valido.\n")

else:
    print(f"El correo {user_gmail} no es valido.\n")
