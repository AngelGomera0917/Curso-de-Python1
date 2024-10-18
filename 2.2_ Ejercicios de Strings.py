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
