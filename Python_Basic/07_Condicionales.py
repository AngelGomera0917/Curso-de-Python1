### Condionales ###

# if, elif, else

print("\n")


my_condition = True

if my_condition: # Si la condicion es verdadera, se ejecuta el bloque de codigo
    print(" Mi primera condicion es verdadera.")
    
my_condition = False

if my_condition: # Si la condicion es falsa, no se ejecuta el bloque de codigo, para que una condicion se ejecute tiene que ser verdadera. 
    print(" Mi segunda condicion es Falsa.")
    
print("\n")

my_condition = 5 * 4

if my_condition > 100: # Esta condicion es falsa porque 5 * 4 = 20 y 20 no es mayor a 100.
    print(" Mi tercera condicion es Falsa.")

my_condition = 5 * 4

if my_condition: # Esto es lo mismo que, if my_condition == 20: porque 5 * 4 = 20... El valor 20 se guarda en la variable my_condition y eso es lo que vale.
    
    print(" Mi cuarta condicion es verdadera.")

print("\n")

my_condition = 17

if my_condition > 10: # Esta condicion es verdadera porque 17 es mayor que 10.
    print("Mi condicion es verdadera.")
    
elif my_condition > 15: # Esta condicion es falsa porque 17 es mayor que 10, y no se ejecuta la primera condicion.
    print("Mi condicion es falsa.") # Esta condicion no se ejecuta porque la primera condicion es verdadera.
    
else: # Si ninguna de las condiciones anteriores se cumple, se ejecuta este bloque de codigo.
    print("Mi condicion es falsa.")
    
print("\n")

print("\n \t Fin del programa.\n")

print("\n")

# Metodo match

Colors = "Azul"

match Colors:
    case "Blanco":
        print(" Mi color favorito es el Blanco")
    
    case "Azul":
        print(" Mi color favorito es el Azul")
    
    case "Verde":
        print(" Mi color favorito es el Verde")

    case "Rojo":
        print(" Mi color favorito es el Rojo")

print("\n")