import hashlib
import time

def main():
    hash_objetivo = "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    contador = 0
    tiempo_inicio = time.perf_counter()
    for h in range(100000000):  # El rango va de 0 hasta 99,999,999
        cadena = f"{h:08d}"

        '''explicacion: cadena.encode() - > pasa la cadena a binario ,
            hashlib.sha256(lo anterior) - > convierte la cadena en binario al objeto interno que maneja la libreria ,
             <lo anterior>.hex_digest - > hace el hash '''
        resultado = hashlib.sha256(cadena.encode()).hexdigest()
        contador += 1
        if resultado == hash_objetivo:
            tiempo_fin = time.perf_counter()
            tiempo_total = tiempo_fin - tiempo_inicio
            hash_seg = contador / tiempo_total
            print(f"coincidencia encontrada: {cadena}")
            print(f"Tiempo(seg): {tiempo_total:.2f} segundos")
            print(f"Tiempo(hash/seg): {hash_seg:.2f} hash/seg")
            break

if __name__ == "__main__":
    main()
