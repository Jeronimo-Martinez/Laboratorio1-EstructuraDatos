from pathlib import Path

def generar_matriz():
    filas = 100000
    columnas = 100000

    fila0 = ("0" * columnas) + "\n" # crear filas de 0s y 1s en ram
    fila1 = ("1" * columnas) + "\n"

    with open("Matriz.txt", "w", encoding="utf-8") as f:
        for _ in range(filas//2):
            f.write(fila0)
            f.write(fila1)

    print(f"matriz guardada en: {Path("Matriz.txt").resolve()}")