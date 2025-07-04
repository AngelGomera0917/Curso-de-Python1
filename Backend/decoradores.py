

                                    # Los Decoradores

# Un decorador es una función que recibe otra función como argumento y devuelve una nueva función que generalmente extiende o modifica el comportamiento de la función original.

def my_decorador(func):
    def show_info():
        print("Amo la programación")
        func()
        print("Mi lenguaje favorito es Python")
    return show_info


@my_decorador
def enviar_greeting():
    print(" Me encanta programar")
    
enviar_greeting()