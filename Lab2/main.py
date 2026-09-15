from arbol_merkle import MerkleTree
import arbol_merkle as mk
from rich import print
from grafico_arbol import mostrar_arbol_matplotlib

def main():
    transacciones = [
        "Maria transfiere 50 dólares",
        "Juan retira 100 dólares",
        "Fabian transfiere 172 dólares",
        "Tatiana recibe 50 dólares",
        "Julian retira 20 dólares"
    ]

    arbol = MerkleTree(transacciones)
    nodo_raiz = arbol.get_raiz()
    arbol_rich = mk.convertir_a_rich(nodo_raiz)

    print("Bloques a partir de los que se construye el arbol:\n")
    for transaccion in transacciones:
        print(transaccion)
    print("\n====== ÁRBOL DE MERKLE =======")
    print(arbol_rich)
    mostrar_arbol_matplotlib(arbol.raiz)

    print(f"\nRaiz del arbol: {nodo_raiz.hash_full}")


    print("\nSi se cambia un dato, también cambia el arbol y la raiz \n ej: dato 2 : Juan retira 100 dólares -> Juan retira 125 dólares")
    transacciones_cambio = transacciones
    transacciones_cambio[1] = "Juan retira 125 dólares"

    arbol_cambio = MerkleTree(transacciones_cambio)
    nodo_raiz_cambio = arbol_cambio.get_raiz()
    arbol_rich_cambio = mk.convertir_a_rich(nodo_raiz)

    print("\n Bloques a partir de los que se construye el arbol:\n")
    for transaccion in transacciones_cambio:
        print(transaccion)
    print("\n====== ÁRBOL DE MERKLE =======")
    print(arbol_rich_cambio)
    mostrar_arbol_matplotlib(arbol_cambio.raiz)

    print(f"\nRaiz del arbol con un dato cambiado: {nodo_raiz_cambio.hash_full}")
    print(f"Raiz del arbol original: {nodo_raiz.hash_full}")


    print("\n=============================================")
    print("prueba en el bloque 3 , arbol original")
    raiz_esperada = nodo_raiz.hash_full
    transaccion_prueba = "Fabian transfiere 172 dólares"
    prueba = arbol.get_proof(2)
    es_valida, raiz_obtenida = MerkleTree.verificar_prueba(transaccion_prueba, prueba, raiz_esperada)

    print(f"\nVerificando '{transaccion_prueba}': \n")
    print(f"[Raíz esperada: {raiz_esperada}")
    print(f"Raíz obtenida:] {raiz_obtenida}")
    print(f"\nResultado: {'EXITO - La transacción es valida' if es_valida else 'FALLO - El hash final no coincide'}\n")


    dato_falso = "Fabian transfiere 2000 euros"
    es_valida, raiz_obtenida = MerkleTree.verificar_prueba(dato_falso, prueba, raiz_esperada)
    print(f"\nVerificando '{transaccion_prueba}': \n")
    print(f"[Raíz esperada: {raiz_esperada}")
    print(f"Raíz obtenida:] {raiz_obtenida}")
    print(f"\nResultado: {'EXITO - La transacción es valida' if es_valida else 'FALLO - El hash final no coincide'}\n")

if __name__ == "__main__":
    main()