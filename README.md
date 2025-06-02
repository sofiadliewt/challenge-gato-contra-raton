# challenge-gato-contra-raton
# 🐁 Simulador de Gato, Ratón y Queso con Minimax

Este proyecto es un simulador en Python de una persecución entre un **ratón inteligente** (IA con algoritmo Minimax) y un **gato controlado por el usuario**. Ambos se mueven en un tablero de 10x10 con el objetivo de alcanzar al ratón o al queso, respectivamente. El primero que lo logre, gana.

---

## 🎮 Cómo se juega

* El **usuario elige la posición inicial del gato** (coordenadas de 0 a 9).
* El **ratón empieza siempre en la esquina superior izquierda (0,0)**.
* El **queso está fijo en la posición (4,4)**.
* El **ratón se mueve solo** usando el algoritmo Minimax.
* El **usuario controla al gato** con las teclas:

  * `w`: arriba
  * `s`: abajo
  * `a`: izquierda
  * `d`: derecha

---

## 🧠 Inteligencia del Ratón

El ratón usa el algoritmo **Minimax con profundidad 8**, evaluando los movimientos futuros tanto del gato como los suyos, con el objetivo de **acercarse al queso y alejarse del gato**.

La función de evaluación (`puntuar_estado`) calcula:

* **Distancia al queso** (entre menos, mejor para el ratón).
* **Distancia al gato** (entre más lejos esté el gato, mejor para el ratón).

---

## 📆 Estructura del Código

### `puntuar_estado(...)`

Evalúa un estado del tablero, devolviendo un valor numérico que guía al algoritmo Minimax.

### `minimax(...)`

Algoritmo recursivo que simula los movimientos del ratón y el gato por turnos. Alterna entre jugador maximizador (ratón) y minimizador (gato) hasta llegar a la profundidad límite o una condición de fin.

### `mostrar_tablero(...)`

Imprime el tablero actual en la consola.

### `mover_gato(...)`

Permite al jugador mover al gato con `w/a/s/d`.

### `pedir_posicion_gato(...)`

Solicita al usuario la posición inicial del gato, validando que esté en el tablero.

### `crear_tablero()`

Crea el tablero vacío de 10x10 con casillas `["[]"]`.

---

## 🔄 Lógica del Juego

El juego se ejecuta en un bucle hasta que:

* El gato atrape al ratón → **Gana el gato**.
* El ratón llegue al queso → **Gana el ratón**.
* Ambos hayan hecho 30 movimientos → **Empate**.

Cada turno, se actualiza el tablero y se muestra al usuario.

---

## ✅ Requisitos

Solo necesitás tener **Python 3** instalado. No se usan librerías externas.

---

## 📷 Ejemplo del Tablero

```
🐁[][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][]🦀[][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][]🐈[]
```



