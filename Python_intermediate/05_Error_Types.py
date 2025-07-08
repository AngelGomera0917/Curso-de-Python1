
# ========================= Error Types ========================= #

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def info(self):
        print(f" Nombre: {self.nombre} ")
        print(f" Edad: {self.edad} ")
        
class educacion:
    def __init__(self, universidad):
        self.universidad = universidad
                
    def info_uni(self):
        print(f" Universidad: {self.universidad} ")
        
class rol:
    def __init__(self, status):
        self.status = status
    
    def info_rol(self):
        print(f" Status: {self.status} ")

class maestro(persona, educacion, rol):
    def __init__(self, nombre, edad, universidad, status, materia ):
        
        persona.__init__(self, nombre, edad)
        educacion.__init__(self, universidad)
        rol.__init__(self, status)
        self.materia = materia
                
    def info_maestro(self):
        print(f" {self.info()} | {self.info_uni()} | {self.info_rol()} | Materia: {self.materia}")

maestro_1 = maestro("Juan Martinez",30,"Intec","Docente", "Plan de Negocios")

maestro_1.info_maestro()



print("\n")

