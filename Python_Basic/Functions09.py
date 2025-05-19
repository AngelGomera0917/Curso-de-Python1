                                                ### Funciones ###

print("\n")

def my_funtion(): # con la palabra reservada def defino una funcion
    print(" Hola, Esto es una funcion funcion\n")

my_funtion() # Llamo a la funcion

print("\n")


# a = input("Ingrese un valor: ") # Pido un valor al usuario
# b = input("Ingrese otro valor: ") # Pido otro valor al usuario

def sum_two_values(first_value , second_values): # Defino la funcion sum_two_values con dos parametros 
    print(first_value + second_values)# Imprimo la suma 

sum_two_values(3, 9) # Llamo a la funcion sum_two_values con los valores ingresados, esta funcion no retorna nada.

print("\n")


def sum_two_values_with_return(first_value , second_values): # Defino la funcion sum_two_values_with_return con dos parametros first_value y second_values
    return first_value + second_values # Retorno la suma de first_value y second_values

result = sum_two_values(3, 4)  

print(result) # En el resultado no retorna nada que es NONE

result = sum_two_values_with_return(5, 11) # Llamo a la funcion con los valores ingresados y guardo el resultado en la variable result para que pueda ser usada # El resultado de la funcion lo tienes que almacenar en una variable para poder usarlo

print(result) # Imprimo el resultado

print("\n") # Esto es un print para separar los resultados


def Print_name (name, surname):
    print(f" {name} {surname} ")

Print_name(surname = "Gomera", name = "Angel") # Reordeno los valores de los parametros


print("\n")

def Print_nam_with_default (name, surname, numero = 17): # Defino una funcion con un parametro por defecto
    print(f" {name} {surname} {numero} ")

Print_nam_with_default (" Angel", "Gomera") # Llamo a la funcion sin el parametro por defecto
Print_nam_with_default (" Angel", "Gomera", 9) # Aqui no le hizo caso al parametro por defecto

print("\n")

def print_texts(*args): # Defino una funcion con un numero indefinido de parametros
    for text in args: # Recorro los parametros
        print(text) # Imprimo los parametros

print_texts("Hola", "Como estas", "Bien", "Gracias") # Llamo a la funcion con los parametros

print("\n")

def print_texts(*text): # Defino una funcion con un numero indefinido de parametros 
    print(text) # Imprimo los parametros

print_texts("Hola", "Como estas", "Bien", "Gracias")

print("\n")

print("\n")


def verificar (numero):
    if numero > 0:
        
        return numero # Devuelve el número positivo

resultado = verificar(6)

print("Número positivo:", resultado) # 6


print("\n")

def verificar (numero):
    if numero < 0:
        
        return  # Sale de la función sin hacer nada
    
    else:
        print("Número positivo:", numero)
    
verificar(5)  # No imprimirá nada


print("\n")

def resta(a, b):
    
    return a - b  # Devuelve la suma

resultado = resta(8, 3)

print(resultado)  # 5

print("\n")

def recomendacion_planta(cuidado):
    
    if cuidado == "bajo":
        return ("Cactus")
    
    elif cuidado == "medio":
        return ("Suculenta")
    
    elif cuidado == "alto":
        return ("Orquídea")
    
    else:
        return "No se encontró ninguna planta"
    
# Evitar ejecución automática al importar
if __name__ == "__main__":
    recomendacion_planta("medio")  # Solo se ejecutará si corres Functionss.py directamente
    retornar = recomendacion_planta("medio")  # Lo guardo dentro de una variable porque la función retorna un valor
    print(retornar)
    
# recomendacion_planta("medio")  # Suculenta, Si aqui ponemos full, imprimira blanco porque no guardamos el valor en la variable
# retornar = recomendacion_planta("full") # Lo guardo dentro de una variable porque la función retorna un valor
# print(retornar)  # No se encontró ninguna planta

print("\n")

