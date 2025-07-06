# Types Hints for the Backend

# es importante para mejorar la legibilidad y mantenibilidad del código, especialmente en proyectos grandes o colaborativos. Aquí hay algunos tipos de datos comunes que puedes usar en Python:
from typing import Dict, List, Tuple, Union, Optional
# Definición de tipos de datos comunes
String = str
Integer = int
Float = float
Boolean = bool
ListOfStrings = List[str]
ListOfIntegers = List[int]

# Es especialmete para para definir y especificar los tipos de datos que se espera que maneje una función o un método. Esto ayuda a los desarrolladores a entender mejor cómo interactuar con el código y qué tipos de datos esperar. Tambien ayuda al backend a validar los datos de entrada y salida, lo que puede prevenir errores y mejorar la calidad del código.

print("\n")

# Le estoy especificando que es un string
my_variable: str = " Mi nombre es Angel y amo la programacion en Python"
print(f"Mi variable es de tipo: {type(my_variable)} y su valor es: {my_variable}")

print("\n")

my_variable: int = 30 # Le estoy especificando que es un entero
print(f"Mi variable es de tipo: {type(my_variable)} y su valor es: {my_variable}")

print("\n")