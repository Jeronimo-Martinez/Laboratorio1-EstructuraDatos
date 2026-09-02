import matriz
import verificaciones as ver

if __name__ == '__main__':

    #matriz.generar_matriz()

    input("presione enter para continuar...")
    #ejemplo quemado

    # Traer 100 elementos de la Fila 2
    ver.traer_elementos_fila(num_fila=1, cantidad_elementos=100)
    input("presione enter para continuar...")

    #traer toda la fila 1
    ver.traer_elementos_fila(num_fila=1)
    input("presione enter para continuar...")

    # Traer 100 elementos de la Fila 2, deberian ser solo 1s
    ver.traer_elementos_fila(num_fila=2, cantidad_elementos=100)
    input("presione enter para continuar...")

    #traer toda la fila 2
    ver.traer_elementos_fila(num_fila=2)
    input("presione enter para continuar...")

    # Traer todos los elementos de la Columna 1
    ver.traer_elementos_columna(num_columna=1)
    input("presione enter para continuar...")

    #traer los 10 primeros elementos de la columna 1
    ver.traer_elementos_columna(num_columna=1, cantidad_elementos=10)
    input("presione enter para continuar...")

    #  Consultar un dato de la Fila 1
    ver.obtener_dato(num_fila=1, num_columna=5)
    #ver en la fila
    ver.traer_elementos_fila(1, 10)
    input("presione enter para continuar...")

    #  Cambiar ese dato por un 1
    ver.modificar_dato(num_fila=1, num_columna=5, nuevo_valor="1")
    input("presione enter para continuar...")

    #  Volver a consultar para verificar cambio
    ver.obtener_dato(num_fila=1, num_columna=5)
    # ver en la fila
    ver.traer_elementos_fila(1, 10)




