import hashlib
from binarytree import Node

def hash(texto: str):
    return hashlib.sha256(texto.encode()).hexdigest()


def construir_arbol_merkle(transacciones):
    if not transacciones:
        return None

    nodos_actuales = []
    for t in transacciones:
        h_full = hash(t)
        nodo = Node(h_full[:5]) # para poder imprimir el arbol
        nodo.hash_full = h_full
        nodos_actuales.append(nodo)

    while len(nodos_actuales) > 1: # funciona como una cola
        siguiente_nivel = []
        i = 0
        while i < len(nodos_actuales):
            if i + 1 < len(nodos_actuales):  #si existe una pareja disponible con la cual concatenar
                izq = nodos_actuales[i]
                der = nodos_actuales[i + 1]

                hash_padre = hash(izq.hash_full + der.hash_full)
                nodo_padre = Node(hash_padre[:5])
                nodo_padre.hash_full = hash_padre
                nodo_padre.left = izq
                nodo_padre.right = der

                siguiente_nivel.append(nodo_padre)
                i += 2
            else:
                # Si n es impar en este nivel, el nodo sobrante sube al siguiente nivel
                siguiente_nivel.append(nodos_actuales[i])
                i += 1

        nodos_actuales = siguiente_nivel

    # La raíz es el único nodo restante
    return nodos_actuales[0]

def main():
    # Ejemplo con n = 5
    transacciones = [
        "git commit initialcomit",
        "git commit undo last commit",
        "git commit redo first commit hotfix",
        "git push origin main",
        "git checkout -b feature"
    ]

    arbol = construir_arbol_merkle(transacciones)
    print("=== ÁRBOL DE MERKLE ===")
    print(arbol)
    print("===========================")
    for nodo in arbol:
        print(nodo.hash_full)


if __name__ == "__main__":
    main()