
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# offset entre elementos de una fila = 1 caracter, no es necesario definir un offset formal ni usar separadores en archivo
# el separador entre filas es un salto de linea (\n). offset entre filas = 100002 bytes, \n(el separador) ocupa 2 bytes en windows
def verificar_matriz():
    archivo = "Matriz.txt"

    print("  ----- total columnas en el archivo -----")

    with open(archivo, "r", encoding="utf-8") as f:

        primera_fila = f.readline() # se lee solo la primera línea

        columnas = len(primera_fila.replace("\n", "").replace("\r", "")) ## reemplaza los \n del archivo con "" y cuenta los datos
        print(columnas)

        print("  ----- total filas en el archivo -----")

        f.seek(0) # regresa al principio del archivo para volver a contar

        # Cuenta las líneas iterando sobre el archivo (esto no carga el archivo en ram)
        total_filas = sum(1 for linea in f)
        print(total_filas)

def traer_elementos_fila(num_fila, cantidad_elementos=100000, archivo="Matriz.txt"):
    if cantidad_elementos == 100000:
        print(f"---- Fila {num_fila} Completa ) ----")
    else:
        print(f"---- Fila {num_fila} (primeros {cantidad_elementos} elementos) ----")

    with open(archivo, "r", encoding="utf-8") as f:
        # se avanza hasta la fila deseada, saltando las otras, es decir no se leen ni cargan en memoria las filas no necesarias
        for _ in range(num_fila - 1): # mientras el numero de fila(offset) no sea el deseado, salta a la siguente fila
            next(f)

        # se lee la fila y se elimina el salto de linea
        fila = f.readline().rstrip('\r\n')

        #se toma la cantidad de elementos deseada
        elementos = fila[:cantidad_elementos]
        print(elementos)

    print("--" * 50 + "\n")

def traer_elementos_columna(num_columna, cantidad_elementos=100000, archivo="Matriz.txt"):
    if cantidad_elementos == 100000:
        print(f"---- Columna {num_columna} Completa ) ----")
    else:
        print(f"---- Columna {num_columna} (primeros {cantidad_elementos} elementos) ----")

    elementos_columna = []

    with open(archivo, "r", encoding="utf-8") as f:
        # itertools.islice se usa para leer solo las primeras n lineas sin procesar el resto
        for linea in itertools.islice(f, cantidad_elementos):

            ## se extrae solo el elemento en la posicion de la columna
            if len(linea) > (num_columna - 1):
                elementos_columna.append(linea[(num_columna - 1)])

    # Si hay menos de 100 elementos se muestra la columna verticalmente
    if len(elementos_columna) <= 100:
        for char in elementos_columna:
            print(char)
    # Si son mas elementos, se imprime horizontal para no colapsar la consola
    else:
        resultado = "".join(elementos_columna)
        print(resultado)

    print("=" * 50 + "\n")

def obtener_dato(num_fila, num_columna, archivo="Matriz.txt"):
    print(f"==== Buscando dato en Fila {num_fila}, Columna {num_columna} ====")

    with open(archivo, "r", encoding="utf-8") as f:
        #se salta hasta la fila deseada sin cargar el resto en ram
        for _ in range(num_fila - 1):
            next(f)

        fila = f.readline() # se lee la fila

        dato = fila[num_columna - 1] # se extrae el dato dentro de la fila en la columna deseada

        print(f"El dato en la coordenada ({num_fila}, {num_columna}) es: '{dato}'\n")
        return dato


def modificar_dato(num_fila, num_columna, nuevo_valor, archivo="Matriz.txt"):
    print(f"==== Modificando Fila {num_fila}, Columna {num_columna} a '{nuevo_valor}' ====")

    # Asegurarnos de que el nuevo valor sea un solo carácter ("0" o "1")
    nuevo_valor = str(nuevo_valor)[0]

    #se usa el modo r+b (lectura y escritura/update).Lo que permite mover el "cursor" libremente  y sobreescribir sobre el archivo en disco duro sin tener que cargar todo en ram
    with open(archivo, "r+b") as f:
        #Calculo para que funcione en linux ya que \n tiene una longitud diferente
        primera_linea = f.readline()
        bytes_por_fila = len(primera_linea)

        # calcular posicion del dato en disco duro
        posicion_cursor = ((num_fila - 1) * bytes_por_fila) + (num_columna - 1)
        f.seek(posicion_cursor)

        # escribir el nuevo valor en el formato del archivo
        f.write(nuevo_valor.encode('utf-8'))

    print(f"Modificación exitosa. El valor ahora es '{nuevo_valor}'.\n")




