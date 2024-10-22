print("\n")

"""Escribir un programa que lea un entero positivo n,introducido por el usuario y después muestre en 
pantalla la suma de todos los enteros desde 1 hasta n. """

"""entero = int(input("Por favor introducir un numero entero: "))

suma = (entero * (entero + 1)) // 2

print(f" La suma de todos los enteros positivos de 1 a n es de: {suma} . ")"""

print("\n")

""" Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice 
de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa 
corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales."""

"""peso = float(input("Por favor introducir su peso en Kilogramos: "))

estatura = float(input("Por favor introducir su estatura en metros: "))

imc = round((peso / (estatura ** 2)), 2)

print(f" El índice de masa corporal es de: {imc} ") """

print("\n")

""" Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión. """

"""cantidad = float(input("Por favor introducir su cantidas a invertir en la propiedad: "))

interes = float(input("Por favor introducir su interes anual: "))

años = int(input("Por favor introducir la cantidad de años: "))

ganancia = round(cantidad * ((1 + (interes / 100)) ** años), 2)

print(f" Su ganancia anual de su inversion sera de: {ganancia} ")"""

print("\n")

''' Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta 
por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el 
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada 
muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
y calcule el peso total del paquete que será enviado. '''

'''payaso = int(input(" Por favor introducir la cantidad de payasos enviados en el ultimo pedido: "))

muñeca = int(input(" Por favor introducir la cantidad de muñecas enviadas en el ultimo pedido: "))

peso_payaso = payaso * 112

peso_muñeca = muñeca * 75

print(f""" Cada payaso pesa 112 g y cada muñeca pesa 75 g, por lo tanto el peso total del paquete es 

de {peso_payaso + peso_muñeca} g.""")'''

print("\n")

""" Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final
de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada
en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por 
pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos 
decimales. """

'''deposito = float(input("Por favor, introducir la cantidad de dinero depositada en la cuenta: "))

interes = 0.04

año1 = round(deposito * (1 + interes), 2)

año2 =  round(año1 * (1 + interes), 2)

año3 =  round(año2 * (1 + interes), 2)

print(f""" \n \tEn su Primer año obtendra: {año1} $

\tEn su Segundo año obtendra: {año2} $

\tEn su Tercer año obtendra: {año3} $ """)'''

print("\n")

""" Una panadería vende barras de pan a 3.49 € cada una. El pan que no es el día tiene un descuento 
del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
por no ser fresca y el coste final total. """

'''pan = int(input("Cuantas barras de pan que no son del dia fueron vendidas? "))

precio = 3.49

descuento = round(pan * 3.49 * 0.6, 2)

total = round(pan * 3.49 * 0.4, 2)

print(f""" \n \tEl precio habitual de una barra de pan es: {precio} €

\tEl descuento que se le hace por no ser fresca es: {descuento} €

\tEl precio total a pagar con su descuento es de: {total} €  """)'''

print("\n")

""" Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido. """

"""name = input("introduzca su nombre por favor: ")
numero = int(input("introduzca un numero entero: "))
junto = (("\n" + "\t" + name + "\n" ) * ( numero))
print(f" {junto} ")"""

print("\n")

""" Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con 
todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en 
mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. """

"""name = input("introduzca su nombre completo por favor: ")

print( "\n 1",name.lower(),
"\n 2",

name.capitalize(), 
"\n 3",

name.title() )"""

print("\n")

""" Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario 
en mayúsculas, y <n> es el número de letras que tienen el nombre. """

"""name = input("colocar su nombre, por favor: ")

letra = len(name)

print(f"El nombre {name.upper()} tiene {letra} letras.")"""

print("\n")

"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension  donde el prefijo 
es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre 
por pantalla el número de teléfono sin el prefijo y la extensión. """

"""numero = input(" por favor, escribir un numero de telefono con este formato  +34-913724710-56: ")

quita = numero[4:-3]

print(f" su numero de telefono es {quita}")"""

print("\n")

""" Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por 
pantalla la frase invertida. """

"""frase = input(" Escribir una frase de su preferencia: ")

invertida = frase[::-1]

print(f" su frase invertida es: {invertida}.")"""

print("\n")

""" Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula. """

"""frase = input("Escribir una frase de su preferencia: ")

vocal = input("Escribir una vocal de su preferencia: ")

mayuscula = vocal.upper()

remplazo = frase.replace(vocal, mayuscula, 1)

print(f" su frase es : {remplazo}")"""

print("\n")

""" Escribir un programa que me permita colocar mi nombre completo en la cosola, luego me pregunte 
por el apellido que quiero cambiar, luego me permita colocar el apellido nuevo. Al final te mostrara 
el nombre completo con el nuevo apellido. """

'''print("\t ======================== * ========================")
print("\t 💹 Actualización de Apellido en Nombre Completo ✅ ")
print("\t ======================== * ========================\n \n \n \n")

nombre_completo = input(" Por favor, introducir su nombre y apellido completos: ")

cambiar_nombre = input("\n Cual es el apellido que desea remplazar? ")

nuevo_apellido = input("\n Cual es el nuevo apellido que desea obtener? ")

remplazar = nombre_completo.replace(cambiar_nombre, nuevo_apellido)

print(f"""\n \t Su nuevo nombre actualizado con su apellido, sera el siguiente: 

\t \t ✅=== * '{remplazar.title()}' * ===✅  \n""")

print("\n")

print("****************************************** ")

print(f"""\nSu antiguo nombre era:

\t ❌ {nombre_completo.title()}. 

Su nuevo nombre actualizado es:

\t ✅ {remplazar.title()}. \n""")

print("****************************************** \n \n \n ") '''


print("\n")

"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""

'''correo = input("\n Digitar su correo electronico solo con dominio @gmail.com: ")

elimina = correo[:-10]

rempla = correo.replace(elimina,"antoniogomera12")

print(f" Su nuevo correo sera: {rempla} ")'''

print("\n")


""" Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta. """

'''compra = input("Introduce los productos de una cesta de la compra, separados por comas: ")

remplazar = compra.replace(",", "\n")

print(remplazar)'''

print("\n")

''' Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y 
muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos
enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros 
y 2 decimales.'''