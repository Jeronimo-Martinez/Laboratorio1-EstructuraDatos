import hashlib
def main(transacciones):
    arbol = []
    for transaccion in transacciones:
        arbol.append(hashlib.sha256(transaccion.encode()).hexdigest()) #h1, h2, h3 y h4

    arbol.append(hashlib.sha256((arbol[0]+arbol[1]).encode()).hexdigest()) #h12
    arbol.append(hashlib.sha256((arbol[2]+arbol[3]).encode()).hexdigest()) #h34
    arbol.append(hashlib.sha256((arbol[4]+arbol[5]).encode()).hexdigest()) #raiz

    print(arbol)
    h = [val[:8] for val in arbol]
    print("\n==================== ÁRBOL DE MERKLE ====================\n")
    print(f"                        [ Raíz: {h[6]}... ]")
    print("                            /          \\")
    print(f"            [ H12: {h[4]}... ]          [ H34: {h[5]}... ]")
    print("                /          \\                              /          \\")
    print(f"     [ H1: {h[0]}... ] [ H2: {h[1]}... ]  [ H3: {h[2]}... ] [ H4: {h[3]}... ]")

if __name__ == "__main__":
    transacciones = ["Ana paga 150", "Luis paga 230", "Carlos paga 80", "Maria paga 95"]
    main(transacciones)
    transacciones = ["Ana paga 150", "Luis paga 999", "Carlos paga 80", "Maria paga 95"]
    main(transacciones)