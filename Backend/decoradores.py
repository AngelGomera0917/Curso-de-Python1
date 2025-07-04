

                                    # Los Decoradores

# Un decorador es una función que recibe otra función como argumento y devuelve una nueva función que generalmente extiende o modifica el comportamiento de la función original.

print("\n")

def my_decorador(func): # Decorador que recibe una función como argumento
    def show_info(): # Función interna que extiende el comportamiento de la función original
        print("Amo la programación") # Mensaje que se imprime antes de llamar a la función original
        func() # Llama a la función original
        print("Mi lenguaje favorito es Python")
    return show_info


@my_decorador # Decorador aplicado a la función enviar_greeting
def enviar_greeting():
    print(" Me encanta programar")
    
enviar_greeting()

print("\n")