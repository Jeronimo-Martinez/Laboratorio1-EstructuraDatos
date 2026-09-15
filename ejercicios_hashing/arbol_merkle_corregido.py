import hashlib
from rich import print
from rich.tree import Tree

class MerkleNode:
    def __init__(self, hash_full, left=None, right=None):
        self.hash_full = hash_full
        self.value = hash_full[:5]  # Primeros 5 caracteres para la vista
        self.left = left
        self.right = right

def calcular_hash(texto: str):
    return hashlib.sha256(texto.encode()).hexdigest()

def construir_arbol_merkle(transacciones):
    if not transacciones:
        return None

    nodos_actuales = []
    for t in transacciones:
        h_full = calcular_hash(t)
        nodo = MerkleNode(h_full)
        nodos_actuales.append(nodo)

    while len(nodos_actuales) > 1:
        siguiente_nivel = []
        i = 0
        while i < len(nodos_actuales):
            if i + 1 < len(nodos_actuales):  # Pareja disponible
                izq = nodos_actuales[i]
                der = nodos_actuales[i + 1]

                hash_padre = calcular_hash(izq.hash_full + der.hash_full)
                nodo_padre = MerkleNode(hash_padre, left=izq, right=der)

                siguiente_nivel.append(nodo_padre)
                i += 2
            else:
                # Si n es impar, el nodo sube al siguiente nivel
                siguiente_nivel.append(nodos_actuales[i])
                i += 1

        nodos_actuales = siguiente_nivel

    return nodos_actuales[0]

def convertir_a_rich(nodo, rama_rich=None):
    """Convierte de forma recursiva nuestra estructura de nodos a un Tree de rich."""
    if nodo is None:
        return None

    # Si es el nodo raíz del árbol
    if rama_rich is None:
        rama_rich = Tree(f"[bold yellow]Raíz:[/bold yellow] [green]{nodo.value}[/green] ([dim]{nodo.hash_full[:8]}...[/dim])")

    if nodo.left:
        sub_izq = rama_rich.add(f"[cyan]Izq:[/cyan] [green]{nodo.left.value}[/green] ([dim]{nodo.left.hash_full[:8]}...[/dim])")
        convertir_a_rich(nodo.left, sub_izq)

    if nodo.right:
        sub_der = rama_rich.add(f"[magenta]Der:[/magenta] [green]{nodo.right.value}[/green] ([dim]{nodo.right.hash_full[:8]}...[/dim])")
        convertir_a_rich(nodo.right, sub_der)

    return rama_rich

def main():
    transacciones = [
        "git commit initialcomit",
        "git commit undo last commit",
        "git commit redo first commit hotfix",
        "git push origin main",
        "git checkout -b feature"  # n = 5 (impar)
    ]

    raiz_node = construir_arbol_merkle(transacciones)
    arbol_rich = convertir_a_rich(raiz_node)

    print("\n=== ÁRBOL DE MERKLE (RICH) ===")
    print(arbol_rich)

if __name__ == "__main__":
    main()