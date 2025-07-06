import multiprocessing

print("\n")

def calcular_cuadrado(numero):
    print(f"El cuadrado de {numero} es {numero * numero}")

if __name__ == '__main__':
    numeros = [1, 2, 3, 4]
    procesos = []

    for n in numeros:
        p = multiprocessing.Process(target=calcular_cuadrado, args=(n,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

print("\n")