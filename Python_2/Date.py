### Date ###

# date es un módulo de Python que nos permite trabajar con fechas y horas.

print("\n")

import datetime # Importo la libreria de fecha y hora.

# Obtenemos la fecha y hora actual.

hora_actual = datetime.datetime.now() # Con el metodo NOW() obtengo la fecha y hora actual.

print( " La Fecha y la Hora actual son: ", hora_actual) # Muestro la fecha y hora actual.

# Para obtener la fecha en formato 'YYYY-MM-DD'

print("\n")


from datetime import datetime # Importo la libreria de fecha y hora, pero aqui lo hago de una manera especifica.

print(datetime.today())

print("\n")


# Para obtener la fecha en formato 'DD-MM-YYYY'

print(datetime.today().strftime('%d-%m-%Y'))

print("\n")

hora = datetime.now() # guardo la fecha y hora actual en la variable hora.

print(hora.year) # Muestro el año.
print(hora.month) # Muestro el mes.
print(hora.day) # Muestro el dia.
print(hora.hour) # Muestro la hora.
print(hora.minute) # Muestro los minutos.
print(hora.second) # Muestro los segundos.
print(hora.timestamp()) # Muestro la fecha y hora en formato timestamp desde 1970 de la epoca UNIX.


print("\n")

# Ahora vamos a crear una funcion para obtener la fecha y hora actual.

from datetime import datetime

hora_fun = datetime.now() # guardo la fecha y hora actual en la variable hora_fun.

def fecha_hora(date):
    print ("Fecha y Hora actual: ", date) # Muestro la fecha y hora actual.
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp()) # Muestro la fecha y hora en formato timestamp desde 1970 de la epoca UNIX.
    
fecha_hora(hora_fun) # Llamo a la funcion fecha_hora y le paso la variable hora_fun.

print("\n") 

# Ahora vamos a crear una fecha para el nuevo año

import datetime

nuevo_ano = datetime.datetime(2021, 1, 1) # Creo una fecha para el nuevo año.

print("Nueva Fecha: ", nuevo_ano) # Muestro la fecha.

print("\n")

# Vamos a trabajar con la funcion TIME

from datetime import time

tiempo = time(22,12,44) # Time es diferente a datetime, solo se trabaja con la hora y hay que rellenatr los campos de hora, minutos y segundos.

print("Hora Propuesta: ", tiempo,"PM") # Muestro la hora.

print("\n")

# Vamos a trabajar con la funcion DATE

from datetime import date

fecha = date(2025, 1, 17) # Date es diferente a datetime, solo se trabaja con la fecha y hay que rellenar los campos de año, mes y dia.

print("Fecha Propuesta: ", fecha) # Muestro la fecha.

print("\n")