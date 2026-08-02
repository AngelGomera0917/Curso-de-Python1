"""
Un script es simplemente un archivo de código (en este caso, un archivo .py) que se ejecuta de principio a fin para realizar una tarea automática — a diferencia de una aplicación con interfaz gráfica, o de código que solo definís pero no corrés directamente.

Script que lee un archivo de log y cuenta cuantos eventos hay de cada tipo
(INFO, WARNING, ERROR, CRITICAL, DEBUG, etc.)

Uso:
    python contar_errores.py ejemplo.log
"""

import sys
from collections import Counter

# Tipos de nivel que vamos a buscar en cada linea del log
NIVELES = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]


def contar_por_tipo(ruta_archivo):
    """Lee el archivo y devuelve un Counter con la cantidad de cada tipo."""
    contador = Counter()

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            for nivel in NIVELES:
                # Si la palabra del nivel aparece en la linea, la contamos
                if nivel in linea:
                    contador[nivel] += 1
                    break  # una linea solo cuenta para un nivel

    return contador




def mostrar_resultado(contador):
    print("\n--- Resumen del log ---")
    total = sum(contador.values())

    if total == 0:
        print("No se encontraron eventos reconocidos en el archivo.")
        return

    # Ordenamos de mayor a menor cantidad
    for nivel, cantidad in contador.most_common():
        print(f"{nivel:10}: {cantidad}")

    print(f"{'TOTAL':10}: {total}")

    # Mostramos especificamente cuantos ERROR y CRITICAL hubo
    errores = contador.get("ERROR", 0) + contador.get("CRITICAL", 0)
    print(f"\nTotal de errores graves (ERROR + CRITICAL): {errores}")


if __name__ == "__main__":
    # Si se pasa el archivo como argumento en la terminal, lo usamos.
    # Si no, usamos "ejemplo.log" por defecto.
    if len(sys.argv) > 1:
        archivo_log = sys.argv[1]
    else:
        archivo_log = "ejemplo.log"

    try:
        resultado = contar_por_tipo(archivo_log)
        mostrar_resultado(resultado)
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{archivo_log}'")
