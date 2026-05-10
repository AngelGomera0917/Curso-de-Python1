def factory_operation(option):
    
    def deposit(balance, amount):
        return balance + amount
    
    def withdraw (balance, amount):
        if amount > balance:
            return None
        
        return balance - amount
    
    default = lambda *args, **kwargs: " >>> Lo sentimos, la opcion NO es valida. "
    
    if option == "deposit":
        return deposit
    
    elif option == "withdraw":
        return withdraw
    
    else:
        return default
    
usuario = input("Digite la operacion que desea realizar (deposit/witdraw): ")

valor1 = float(input("Digite el valor de Balance: "))

valor2 = float(input("Digite el valor de Amount: "))

print("\n")

funtion = factory_operation(usuario)

print( "El resultado es:", int(funtion(valor1,valor2)))