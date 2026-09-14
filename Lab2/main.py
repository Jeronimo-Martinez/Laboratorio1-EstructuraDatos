from arbol_merkle import MerkleTree
import arbol_merkle as mk
from rich import print

def main():
    transacciones = [
        "Maria transfiere 50 dolares",
        "Juan retira 100 dolares",
        "Fabian transfiere 172 dolares",
        "Tatiana recibe 50 dolares",
        "Julian retira 20 dollares"
    ]

    arbol = MerkleTree(transacciones)
    nodo_raiz = arbol.get_raiz()
    arbol_rich = mk.convertir_a_rich(nodo_raiz)

    print("\n====== ÁRBOL DE MERKLE =======")
    print(arbol_rich)


    print(f"Raiz del arbol: {nodo_raiz.hash_full}")


    transaccion_prueba = "Tatiana recibe 50 dolares"
    prueba = arbol.get_proof(transaccion_prueba)

    print(f"Prueba de inclusion para {transaccion_prueba}")
    for i, (pos, h) in enumerate(prueba):
        print(f"Paso {i + 1}: Agregar hash a la {pos} -> {h[:10]}...")

    es_valida = MerkleTree.verificar_prueba(transaccion_prueba, prueba, nodo_raiz.hash_full)
    print(f"\nVerificando '{transaccion_prueba}':",
          "EXITO - La transaccion es valida" if es_valida else "FALLO - El hash final no coincide")

    dato_falso = "Tatiana recibe 150 dolares"
    es_valida_falsa = MerkleTree.verificar_prueba(dato_falso, prueba, nodo_raiz.hash_full)
    print(f"Verificando '{dato_falso}':",
          "EXITO - La trasaccion es valida" if es_valida_falsa else "FALLO - El hash final no coincide")

if __name__ == "__main__":
    main()