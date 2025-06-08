# 🐱🐭 Simulador de Persecución: Gato vs Ratón

Este proyecto es un **simulador de persecución en un tablero 10x10** entre un **gato controlado por el jugador** y un **ratón controlado por inteligencia artificial usando el algoritmo Minimax**.

---

## 🎯 Objetivo del juego

- El **ratón (🐁)** quiere escapar del gato, y se mueve automáticamente usando **Minimax**.
- El **gato (🐈)** es controlado por el usuario mediante el teclado (WASD) y debe atrapar al ratón.
- Gana el ratón si pasan 30 turnos sin ser atrapado. Gana el gato si atrapa al ratón.

---

## 🧠 Algoritmo usado

Se implementa **Minimax sin poda alfa-beta**, con las siguientes características:

- El ratón (jugador maximizador) evalúa todas sus posibles posiciones.
- El gato (jugador minimizador) también genera todos sus movimientos posibles en la simulación.
- La evaluación se basa en la **distancia de Manhattan** entre ambos.
- La función `puntuar_estado()` devuelve:
  - `+1000` si el ratón sobrevive 30 turnos.
  - `-1000` si el gato atrapa al ratón.
  - Caso contrario, retorna la distancia entre ambos.

---

## 🕹️ Controles

El jugador mueve al gato usando:
- `w`: arriba
- `s`: abajo
- `a`: izquierda
- `d`: derecha

---

## 🧩 Funcionalidades implementadas

- Tablero dinámico de 10x10 impreso por consola.
- Algoritmo Minimax para el movimiento del ratón.
- Control manual del gato por el usuario.
- Finalización automática del juego según condiciones.
- Lógica de turnos.

---

## 📂 Estructura del código

- `minimax()`: implementa la recursión para el cálculo del mejor movimiento del ratón.
- `puntuar_estado()`: evalúa qué tan favorable es el estado actual del juego para el ratón.
- `mover_gato()`: captura las teclas del usuario y aplica la lógica de movimiento.
- `obtener_pos_movimientos()`: calcula movimientos válidos dentro del tablero.
- `mostrar_tablero()`: imprime el estado actual del juego.

---

## ▶️ Cómo ejecutar

1. Asegurate de tener **Python 3** instalado.
2. Copiá el código en un archivo llamado `gato_raton.py`.
3. Ejecutalo con:

```bash
python gato_raton.py
