function resolverNReinas(n) {
  // Creamos una matriz de n x n llena de puntos (.)
  // El punto representa una casilla vacía.
  const soluciones = []; // Creamos un arreglo para almacenar las soluciones encontradas. En este caso, solo almacenaremos la primera solución encontrada, pero podríamos modificar el código para almacenar todas las soluciones si lo deseamos.
  const tablero = Array.from({ length: n }, () => Array(n).fill(".")); // Esta forma de crear el tablero es más eficiente que usar un bucle for tradicional. Utiliza Array.from para generar un array de longitud n, y cada elemento es a su vez un array de longitud n lleno de puntos ("."). Esto evita la necesidad de anidar bucles for para inicializar el tablero, lo que hace que el código sea más limpio y fácil de entender. Además, al usar fill("."), se asegura que cada casilla del tablero esté correctamente inicializada con un punto, representando una casilla vacía.

  function esSeguro(fila, col) {
    // Creamos una función a la cual le pasamos la fila y columna donde queremos colocar la reina, y esta función verificará si es seguro colocarla en esa posición.
    // Verificamos la columna
    // Utilizamos un bucle for para verificar si hay una reina ("R") en la misma columna por encima de la fila actual. Si encontramos una reina, retornamos false, indicando que no es seguro colocar una reina en esa posición. Este método es eficiente porque solo necesitamos revisar las filas anteriores, ya que las filas siguientes aún no han sido procesadas y no pueden contener reinas.
    for (let i = 0; i < fila; i++) {
      if (tablero[i][col] === "R") return false;
    }
    // Verificamos la Diagonal superior izquierda
    // Este bucle for verifica la diagonal superior izquierda desde la posición actual (fila, col). Comienza desde la fila anterior (fila - 1) y la columna anterior (col - 1) y se mueve hacia arriba y hacia la izquierda. Si encuentra una reina ("R") en esta diagonal, retorna false, indicando que no es seguro colocar una reina en esa posición. Este método es eficiente porque solo revisa las posiciones relevantes en la diagonal, evitando la necesidad de revisar toda la matriz.
    for (let i = fila - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
      if (tablero[i][j] === "R") return false;
    }
    // Verificamos la Diagonal superior derecha
    // Utilizamos otro bucle for para verificar la diagonal superior derecha desde la posición actual (fila, col). Comienza desde la fila anterior (fila - 1) y la columna siguiente (col + 1) y se mueve hacia arriba y hacia la derecha. Si encuentra una reina ("R") en esta diagonal, retorna false, indicando que no es seguro colocar una reina en esa posición. Este método es eficiente porque solo revisa las posiciones relevantes en la diagonal, evitando la necesidad de revisar toda la matriz.
    for (let i = fila - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
      if (tablero[i][j] === "R") return false;
    }
    return true; // Si no se encuentra ninguna amenaza, retornamos true, indicando que es seguro colocar una reina en esa posición.
  }

  function colocarReina(fila) {
    // Creamos una función a la cual le pasamos la fila actual donde queremos colocar la reina, y esta función intentará colocar una reina en esa fila y luego llamará recursivamente a sí misma para colocar reinas en las filas siguientes.
    if (fila === n) {
      // Si hemos colocado reinas en todas las filas, significa que hemos encontrado una solución válida.
      // Guardamos una copia del tablero terminado
      soluciones.push(tablero.map((f) => [...f])); // Aquí utilizamos map para crear una nueva matriz que es una copia del tablero actual. Cada fila del tablero se copia utilizando el operador de propagación (...), lo que garantiza que cada fila sea un nuevo array independiente. Esto es importante para evitar que futuras modificaciones al tablero afecten la solución almacenada en el arreglo soluciones.
      return true; // Encontramos una solución
    }

    for (let col = 0; col < n; col++) {
      // Probamos todas las columnas en la fila actual para colocar una reina. Este bucle for itera a través de cada columna en la fila actual, intentando colocar una reina en cada posición posible. Esto es esencial para explorar todas las combinaciones posibles de colocación de reinas en el tablero.
      if (esSeguro(fila, col)) {
        // Verificamos si es seguro colocar una reina en esa posicion. Llamamos a la función esSeguro para verificar si colocar una reina en la posición (fila, col) es seguro. Si es seguro, procedemos a colocar la reina en esa posición.
        tablero[fila][col] = "R"; // 1. Tablero donde se van ubicando

        if (colocarReina(fila + 1)) return true; // Si queremos solo una solución

        tablero[fila][col] = "."; // Backtracking (quitar si no sirve)
      }
    }
    return false; // No se encontró una solución en esta configuración, por lo que retornamos false para indicar que debemos retroceder y probar otra posición para la reina en la fila actual.
  }

  colocarReina(0); // Iniciamos la recursión para colocar reinas en la primera fila
  return soluciones[0]; // Retornamos la primera solución encontrada. Si queremos todas las soluciones, podríamos retornar el arreglo completo soluciones en lugar de solo la primera solución.
}

// Ejecución para N = 8
const N = 8;
const tableroFinal = resolverNReinas(N); // 1. Tablero donde se van ubicando las reinas

// 2. Tablero terminado con todas las reinas ubicadas
console.log("Tablero Final:");
console.table(tableroFinal);

// 3. Arreglo donde se vean los índices de cada reina [fila, columna]
const indicesReinas = tableroFinal.map((fila, i) => [i, fila.indexOf("R")]);
console.log("Índices planteados (Fila, Columna):", indicesReinas);
