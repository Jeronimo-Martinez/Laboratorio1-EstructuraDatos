### Explicación archivos 

**matriz.py** : código que genera y guarda la matriz en memoria.

**verificaciones.py** : colección de funciones para visualizar,verificar y manipular la matriz. 

- ***verificar_matriz()*** : verifica que el tamaño de la matriz sea correcto.
  
- ***traer_elementos_fila(num_fila, cantidad_elementos= 100000)*** : imprime en consola los  primeros <cantidad_elementos> elementos en la fila numero <num_fila>.Si no se especifica la cantidad de elementos , se muestra toda la fila por defecto.
- ***traer_elementos_columna(num_columna, cantidad_elementos= 100000)*** : imprime en consola los  primeros <cantidad_elementos> elementos en la fila numero <num_columna>.Si no se especifica la cantidad de elementos , se muestra toda la columna por defecto.
- ***obtener_dato(num_fila,num_columna,archivo="Matriz.txt)*** : retorna e imprime en consola el valor de la matriz en la posición [<num_fila>,<num_columna>].
- ***modificar_dato(num_fila, num_columna, nuevo_valor, archivo="Matriz.txt")*** : modifica el valor de la matriz en la posición[<num_fila>,<num_columna>] , luego lo imprime en consola y lo retorna.

 ### **Explicación estructura archivo** 
 
 - Matriz binaria de 100,000 x 100,000 (~10 GB) organizada con offsets fijos por fila en disco.
 La matriz se guarda en un archivo .txt donde una fila es la secuencia de unos y ceros , utilizando \n como separador entre filas.
 
 *offset* (entre filas) = 100000 bytes (datos) + 2 bytes (separador \n, windows lo cuenta en 2 bytes) = 100002 bytes  
 - fila 1 : Empieza en el byte 0 
 - fila 2 : empieza en el byte 100002
 - fila 3 : empieza en el byte 200004



 ### ¿Como verificar el contenido de la matriz?
   - vscode y pycharm me permitieron abrir y ver el archivo
   - El codigo tiene un ejemplo quemado que muestra fragmentos de la matriz, editar main.py para recorrer matriz o modificar. 
   - En el interprete de python o la terminal se pueden importar los archivos como módulos y se pueden ejecutar funciones independientemente para navegar sobre la matriz y modificarla.

ej: (en powershell) 

         cd "<ruta de la carpeta Laboratorio1 > "
         py

luego de entrar al interprete de python: 

         import matriz
         import verificaciones as ver
        
          ver.obtener_dato(1, 5)
     
          ver.traer_elementos_fila(1, 10)
     
          ver.modificar_dato(1, 5, "1")


          ver.obtener_dato(1, 5)

o: 

    from verificaciones import modificar_dato, obtener_dato
    modificar_dato(1, 5, "0")
