### Clases y Objetos en Python ###

# Las clases y objetos, son conceptos fundamentales en la programación orientada a objetos. Una clase es un plano, una plantilla, un modelo para crear objetos. Un objeto es una instancia de una clase. Cuando se crea un objeto, se crea una copia de la clase, se asigna memoria para el objeto y se inicializan los atributos del objeto.

print("\n")


print("\n")

class cachorro ():
    def __init__(self, nombre, raza, edad, sexo, color):
        
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.color = color
    
        

camilo = cachorro("Camilo", "Pastor Aleman", "2 años,", "Macho", "Negro. " )
print(camilo.nombre, "es un", camilo.raza, "de", camilo.edad, "es", camilo.sexo, "y es de color", camilo.color);

print("\n")

print("\n")


class cachorro ():
    def __init__(self, nombre, raza, edad, sexo, color):
        
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.color = color
        
    def definicion (self):
        
        ''' Lo recomendable seria poner self.(las variables) self.nombre, porque asi podriamos instanciar otros objetos
        de la misma funcion.'''
        print(pedro.nombre, "es un", pedro.raza, "de", pedro.edad, "es", pedro.sexo, "y es de color", pedro.color);

pedro = cachorro("Pedro", "Pitbull", "4 años,", "Macho", "Crema. " )

pedro.definicion()

print("\n")

print("\n")


class carross():
    def __init__(self, modelo, año, color, documento, costo):
        
        self.modelo = modelo
        self.año = año
        self.color =  color
        self.documento = documento
        self.costo =  costo
        
    def camion (self):
        
        # Self, hace referencia a la instancia del objeto.
        print(f"Yo necesito comprar un carro {self.modelo} del año {self.año}, pero me gustaria de color {self.color} y que los documentos esten {self.documento}, que cueste por lo menos {self.costo}.")

    
    

# Este es un objeto instanciado de la clase carross
vehiculo = carross ("Civic", "2021", "Negro", "Al dia", "RD$ 2,500,000.00")

print("\n")

vehiculo.camion()

print("\n")

car_2 = carross ("Corolla", "2018", "Crema", "Al dia", "RD$ 1,000,000.00")

car_2.camion()

print("\n")

print("El",vehiculo.modelo, "es mi carro Favorito.")

print("\n")

# Este es un objeto instanciado de la clase carross
vehiculo_2 = carross ("Acord", "2024", "Blanco", "Al dia", "RD$ 4,500,000.00")

vehiculo_2.camion()


print("\n")


class cuenta_Bancaria():
    def __init__(self, saldo):  # Método constructor
        self.saldo = saldo # Asigna el saldo inicial
        
    def obtener_saldo(self): # Método para obtener el saldo
        return self.saldo # Devuelve el saldo
    
cuenta = cuenta_Bancaria (1000) # Crear una cuenta con 1000 de saldo
print("Mi cuenta tiene $",cuenta.obtener_saldo()) # Me imprime 1000 porque lo puse dentro de un print () para que retorne.

print("\n")

cuenta2 = cuenta_Bancaria (2000)
print("Mi cuenta tiene $",cuenta2.obtener_saldo())

print("\n")

cuenta2.saldo = 1500 # Aqui lo que hicimos fue modificar el saldo de la cuenta2
print("Mi cuenta tiene $",cuenta2.obtener_saldo())

print("\n")

                                            # Curso de MoureDev

class persona():
    def __init__(self, nombre, apellido, genero):
        self.Completo = f"{nombre} {apellido} {genero}" # Creo una variable que contenga el nombre, apellido y genero de la persona.

person = persona ("Angel", "Gomera,", "Masculino. ") # Creo un objeto de la clase persona.
print(person.Completo)


print("\n")

        # *========================* Actividad Extra *========================*

# Crear una clase para vender un coche y me verifique si esta vendido o no, y si esta vendido, que me imprima un mensaje de que el coche ya fue vendido.

class car_sales(): # Defino la clase car_sales para las ventas de autos.
    def __init__(self, vehiculo, modelo, año, color, propietario): # Método constructor que inicializa los atributos del objeto.
        
        self.vehiculo = vehiculo
        self.modelo = modelo
        self.año = año
        self.color = color
        self.propietario = propietario
        
    def vehicle_description(self): # Método para mostrar la descripción del vehículo.
        
        print(f" Vehículo disponible en el dealer JF Amador: {self.vehiculo} {self.modelo} año {self.año}, color {self.color}. ¡Propietario actual: {self.propietario}!") # Imprime la descripción del vehículo.
        
    def vendido(self, new_owner): # Método para marcar el vehículo como vendido y actualizar el propietario.
        self.new_owner = new_owner
        print(f"Auto {self.vehiculo} {self.modelo} año {self.año}, color {self.color} Vendido a {self.new_owner} ✅") # Imprime un mensaje indicando que el vehículo ha sido vendido y muestra el nuevo propietario.

auto_1 = car_sales("Toyota", "Corolla", "2022", "Blanco", "JF Amador") # Crea un objeto de la clase car_sales para el primer auto.

auto_2 = car_sales("Honda", "Civic", "2024", "Negro", "JF Amador") # Crea un objeto de la clase car_sales para el segundo auto.

auto_1.vehicle_description() # Llama al método vehicle_description del primer auto para mostrar su descripción.

print("\n")

auto_1.vendido("Darli M.") # Llama al método vendido del primer auto para marcarlo como vendido y mostrar el nuevo propietario.

print("\n")

auto_2.vehicle_description() # Llama al método vehicle_description del segundo auto para mostrar su descripción.

print("\n")

auto_2.vendido("Angel Antonio") # Llama al método vendido del segundo auto para marcarlo como vendido y mostrar el nuevo propietario.

print("\n")

# *========================* La Herencia en Python *========================*

# La Herencia en Python permite crear una nueva clase que hereda atributos y métodos de una clase existente. Esto es útil para reutilizar código y crear jerarquías de clases. A esta nueva clase se le llama clase hija o subclase, y a la clase de la que hereda se le llama clase padre o superclase.
                                                                        
class persona():
    def __init__(self, nombre, edad):                                       
        self.nombre = nombre
        self.edad = edad                     
            
    def get_person_info(self):
        return f" Mi Nombre es {self.nombre} y tengo {self.edad} años de edad. "

    
class educacion(persona):  # La clase educacion hereda de la clase persona.
    def __init__(self, nombre, edad, carrera_universitaria, universidad):
        super().__init__(nombre, edad)
        self.carrera_universitaria = carrera_universitaria
        self.universidad = universidad
        
    def describe_profession(self):
        return f" Soy {self.nombre} y tengo {self.edad} años de edad, y me encanta la carrera de {self.carrera_universitaria} en la universidad {self.universidad}."


student_profile_1 = educacion("Angel Antonio", 22, "Desarrollo de Software", "ITLA")

student_profile_2 = educacion("Darli Mariela", 21, "Lenguas Modernas", "UTESA")

print(student_profile_1.get_person_info(), "\n")
print(student_profile_1.describe_profession(), "\n")


print(student_profile_2.get_person_info(), "\n")
print(student_profile_2.describe_profession(), "\n")

        #*========================* Herencia Multiple *========================*
# La herencia múltiple en Python permite que una clase herede de más de una clase padre. Esto puede ser útil para combinar comportamientos de diferentes clases, pero también puede complicar el diseño del código si no se maneja adecuadamente.
# En Python, la herencia múltiple se logra especificando múltiples clases en la definición de la clase hija. Sin embargo, es importante tener cuidado con el orden de las clases padre y cómo se resuelven los conflictos de nombres.

# Clase base Nombre
class Nombre():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def info(self):
        return f" Nombre: {self.nombre} | Edad: {self.edad}. "

print("\n")

# Clase Universidad
class universidad():
    def __init__(self, nombre_universidad):
        self.nombre_universidad = nombre_universidad
        
    def info_universidad(self):
        return f" Universidad: {self.nombre_universidad}. "
        
print("\n")

class RoleStatus():
    def __init__(self, estatus):
        self.estatus = estatus
        
    def puesto(self):
        return f" Posicion: {self.estatus}"

        
# Clase Maestro (herencia múltiple)
class Maestro(Nombre, universidad, RoleStatus):
    def __init__(self, nombre, edad, nombre_universidad, estatus, materia):
        Nombre.__init__(self, nombre, edad)  # Llamada explícita al constructor de la clase Nombre
        universidad.__init__(self, nombre_universidad)  # Llamada explícita al constructor de la clase universidad
        RoleStatus.__init__(self, estatus)
        self.materia = materia
        
        
    def info_maestro(self):
        print(f" {self.info()} | {self.info_universidad()} | {self.puesto()} | Materia: {self.materia} ")
        
print("\n")


class Estudiante(Nombre, universidad, RoleStatus):
    def __init__(self, nombre, edad, nombre_universidad, estatus, carrera):
        Nombre.__init__(self, nombre, edad)  # Llamada explícita al constructor de la clase Nombre
        universidad.__init__(self, nombre_universidad)  # Llamada explícita al constructor de la clase universidad
        RoleStatus.__init__(self, estatus)
        self.carrera = carrera
        
    def info_estudiante(self):
        print(f" {self.info()} | {self.info_universidad()} | {self.puesto()} | Educacion: {self.carrera} ")


# Ejemplo de uso
maestro1 = Maestro("Darli Mariela", 21,"UTESA", "Maestra", "Lenguas Modernas")
estudiante1 = Estudiante("Angel Antonio", 23, "ITLA", "Estudiante", "Desarrollo De Software")

maestro1.info_maestro()

print("\n")

estudiante1.info_estudiante()

print("\n")


import threading

def tarea():
    print("Ejecutando tarea en hilo por Angel Gomera:", threading.current_thread().name)

# Crear hilos
hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar que terminen
hilo1.join()
hilo2.join()

print("\n")


# from PIL import Image, ImageFilter, ImageEnhance
# import threading

# # Cargar imagen base
# imagen_base = Image.open("imagen_original.jpg")

# # Función para aplicar efectos
# def aplicar_efecto(nombre_efecto, funcion_efecto):
#     imagen_modificada = funcion_efecto(imagen_base.copy())
#     imagen_modificada.save(f"{nombre_efecto}.jpg")
#     print(f"{nombre_efecto} generado")

# # Lista de efectos con funciones
# efectos = [
#     ("blanco_y_negro", lambda img: img.convert("L")),
#     ("bordes", lambda img: img.filter(ImageFilter.FIND_EDGES)),
#     ("brillo_alto", lambda img: ImageEnhance.Brightness(img).enhance(2.0)),
#     ("contraste_bajo", lambda img: ImageEnhance.Contrast(img).enhance(0.5)),
#     ("enfocado", lambda img: img.filter(ImageFilter.SHARPEN)),
# ]

# # Crear y lanzar hilos
# hilos = []
# for nombre, funcion in efectos:
#     hilo = threading.Thread(target=aplicar_efecto, args=(nombre, funcion))
#     hilos.append(hilo)
#     hilo.start()

# # Esperar a que todos terminen
# for hilo in hilos:
#     hilo.join()

# print("Todas las imágenes han sido procesadas.")