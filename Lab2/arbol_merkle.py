import hashlib
from rich.tree import Tree


class MerkleNode:
    def __init__(self, hash_full, left=None, right=None):
        self.hash_full = hash_full
        self.value = hash_full[:5]
        self.left = left
        self.right = right



class MerkleTree:
    def __init__(self, transacciones):
        # se construye el árbol y se guarda la raíz
        self.transacciones = transacciones
        self.raiz = self._construir_arbol(transacciones)

    def _calcular_hash(self, texto: str):
        return hashlib.sha256(texto.encode()).hexdigest()

    def _construir_arbol(self, transacciones):
        if not transacciones:
            return None

        nodos_actuales = []
        for t in transacciones:
            h_full = self._calcular_hash(t)
            nodo = MerkleNode(h_full)
            nodos_actuales.append(nodo)

        while len(nodos_actuales) > 1:
            # Si el nivel es impar, duplica el último nodo
            if len(nodos_actuales) % 2 != 0:
                ultimo_nodo = nodos_actuales[-1]
                nodos_actuales.append(ultimo_nodo)

            siguiente_nivel = []
            i = 0

            while i < len(nodos_actuales):
                izq = nodos_actuales[i]
                der = nodos_actuales[i + 1]

                hash_padre = self._calcular_hash(izq.hash_full + der.hash_full)
                nodo_padre = MerkleNode(hash_padre, left=izq, right=der)

                siguiente_nivel.append(nodo_padre)
                i += 2

            nodos_actuales = siguiente_nivel

        return nodos_actuales[0]

    def get_raiz(self):
        """Retorna el nodo raíz del árbol."""
        return self.raiz

    def get_proof(self, transaccion):
        """Genera la prueba de inclusión para una transacción dada."""
        try:
            # Buscar el índice de la transacción
            index = self.transacciones.index(transaccion)
        except ValueError:
            return None  # La transacción no está en el árbol

        # Recreamos el proceso de subida nivel por nivel usando solo los hashes
        hashes_actuales = [self._calcular_hash(t) for t in self.transacciones]
        prueba = []

        while len(hashes_actuales) > 1:
            if len(hashes_actuales) % 2 != 0:
                hashes_actuales.append(hashes_actuales[-1])

            #determinar posicion nodo actual , hijo izq o der
            if index % 2 == 0:
                posicion_hermano = "right"
                hermano_idx = index + 1
            else:
                posicion_hermano = "left"
                hermano_idx = index - 1

            # Guardar la posición y el hash del hermano necesario
            prueba.append((posicion_hermano, hashes_actuales[hermano_idx]))

            siguiente_nivel = []
            for i in range(0, len(hashes_actuales), 2):
                hash_padre = self._calcular_hash(hashes_actuales[i] + hashes_actuales[i + 1])
                siguiente_nivel.append(hash_padre)

            hashes_actuales = siguiente_nivel
            index = index // 2  #indice del nuevo nodo padre

        return prueba

    @staticmethod
    def verificar_prueba(transaccion, prueba, hash_raiz_esperado):
        """Verifica si la transacción pertenece al árbol usando la prueba."""
        if prueba is None:
            return False

        # Hacemos hash de la transacción original
        hash_actual = hashlib.sha256(transaccion.encode()).hexdigest()

        # Reconstruir el camino hacia la raíz
        for posicion, hash_hermano in prueba:
            if posicion == "right":
                # Si el hermano se va a la derecha, se toma el nodo izq
                texto_a_hashear = hash_actual + hash_hermano
            else:
                # Si el hermano va a la izq, se toma el nodo der
                texto_a_hashear = hash_hermano + hash_actual

            hash_actual = hashlib.sha256(texto_a_hashear.encode()).hexdigest()

        # Compar el hash resultante con la raíz pública del árbol
        return hash_actual == hash_raiz_esperado


def convertir_a_rich(nodo, rama_rich=None):
    """Convierte de forma recursiva nuestra estructura de nodos a un Tree de rich."""
    if nodo is None:
        return None

    if rama_rich is None:
        rama_rich = Tree(
            f"[bold yellow]Raíz:[/bold yellow] [green]{nodo.value}[/green] ([dim]{nodo.hash_full[:8]}...[/dim])")

    if nodo.left:
        sub_izq = rama_rich.add(
            f"[cyan]Izq:[/cyan] [green]{nodo.left.value}[/green] ([dim]{nodo.left.hash_full[:8]}...[/dim])")
        convertir_a_rich(nodo.left, sub_izq)

    if nodo.right:
        sub_der = rama_rich.add(
            f"[magenta]Der:[/magenta] [green]{nodo.right.value}[/green] ([dim]{nodo.right.hash_full[:8]}...[/dim])")
        convertir_a_rich(nodo.right, sub_der)

    return rama_rich

