import matplotlib.pyplot as plt
import networkx as nx

def mostrar_arbol_matplotlib(nodo_raiz):
    """Genera y muestra el diagrama del Árbol de Merkle usando Matplotlib y NetworkX."""
    if nodo_raiz is None:
        print("El árbol está vacío.")
        return

    G = nx.DiGraph()
    pos = {}
    labels = {}

    # Función interna para asignar posiciones (x, y) de forma recursiva
    def calcular_posiciones(nodo, x=0.5, y=1.0, dx=0.25):
        if nodo is None:
            return

        nodo_id = id(nodo)  # ID único en memoria
        G.add_node(nodo_id)
        pos[nodo_id] = (x, y)
        labels[nodo_id] = f"{nodo.value}\n({nodo.hash_full[:6]})"

        if nodo.left:
            hijo_izq_id = id(nodo.left)
            G.add_edge(nodo_id, hijo_izq_id)
            calcular_posiciones(nodo.left, x - dx, y - 0.25, dx / 2)

        if nodo.right:
            hijo_der_id = id(nodo.right)
            G.add_edge(nodo_id, hijo_der_id)
            calcular_posiciones(nodo.right, x + dx, y - 0.25, dx / 2)

    # 1. Construir el grafo y calcular las posiciones
    calcular_posiciones(nodo_raiz)

    # 2. Configurar el lienzo de Matplotlib
    plt.figure(figsize=(10, 6))
    plt.title("Estructura del Árbol de Merkle - Simplificado(sin duplicados)", fontsize=14, fontweight="bold")

    # 3. Dibujar los nodos y las conexiones
    nx.draw(
        G,
        pos,
        labels=labels,
        with_labels=True,
        node_size=3500,
        node_color="#87CEEB",  # Azul claro
        node_shape="s",        # Formato de caja/cuadrado
        font_size=8,
        font_weight="bold",
        arrows=True,
        arrowstyle="-|>",
        arrowsize=12,
        edge_color="gray"
    )

    plt.axis("off")  # Ocultar los ejes cartesianos
    plt.tight_layout()
    plt.show()      # Abre la ventana interactiva