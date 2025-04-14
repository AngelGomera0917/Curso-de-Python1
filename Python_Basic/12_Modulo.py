
""" Modulos. """ # Son librerias que tiene creada el propio sistema o lenguaje.

# Cuando nosotros tenemos algun codigo externo a nuestro fichero o proyecto y queremos utilizarlo, aqui entra el concepto de modulos. 

# Un módulo en Python es un archivo que contiene definiciones de funciones, variables y clases, que puedes importar y usar en otros programas. Los módulos permiten organizar y reutilizar el código de manera más eficiente.


print("\n")

                        # Aqui importe mi modulo externo, para poder usar todas sus funciones y variables definidas en el modulo

import My_Module 

My_Module.sumValue(6, 7, 9) # Imprimo una variable que esta en mi modulo externo

print("Mi Resultado es: ",My_Module.multiplicar(6, 5)) # Lo pongo dentro de un PRINT porque es un RETURN que estoy utilizando.

print("\n")

                        # Aqui importo una sola funcion del modulo externo, especifico la funcion a utilizar.

from My_Module import printvalue 

printvalue(" Soy Estudiante de Desarrollo de Software. ") # Imprimo la variable que esta en mi modulo externo

# sumValue(10, 12,4) - Esta es un ERROR porque solo importe una funcion especificada.

print("\n")

                                # Aqui importo una sola funcion del modulo externo, especifico la funcion a utilizar.
                                # Y creo una variable nueva para guardar el resultado.

from Module2 import planta as Nivel_Planta 

Nivel_Planta("alto")
print("\n")

                                        # Modulos del sistema de Python... 


print("\tModulos del sistema de Python...\n")


        # Este modulo math proporciona funciones matemáticas como raíces cuadradas, trigonometría, logaritmos y constantes como π (pi).

import math as matematica # Nombro mi libreria Math como MATEMATICA.

print("El valor de PI es: ", matematica.pi, "\n") # Esta funcion me dice el valor el PI
print("Mi potencia es de: ",matematica.pow(3, 2)) # Este me busca la potencia


                                # Este modulo random proporciona funciones para generar números aleatorios.

import random

print("\nUn número aleatorio es: ", random.randint(1, 100), "\n")



from math import pi as Pi_Value # Le estoy dando un nombre muy concreto al valor que estoy importando.

print("El valor de PI es: ", round(Pi_Value,2), "\n") # Con el round le digo que solo quiero 2 decimales.



