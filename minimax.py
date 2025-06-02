def puntuar_estado(posicion_raton, posicion_gato, posicion_queso):
    distancia_al_queso = abs(posicion_raton[0] - posicion_queso[0]) + abs(posicion_raton[1] - posicion_queso[1])
    distancia_al_gato = abs(posicion_raton[0] - posicion_gato[0]) + abs(posicion_raton[1] - posicion_gato[1])
    return -distancia_al_queso + distancia_al_gato


def minimax(pos_raton, pos_gato, pos_queso, profundidad, maximizador):
    if profundidad == 0 or pos_raton == pos_gato or pos_raton == pos_queso:
        return puntuar_estado(pos_raton, pos_gato, pos_queso), pos_raton

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if maximizador:
        mejor_valor = float('-inf')
        mejor_mov = pos_raton
        for dx, dy in movimientos:
            nuevo_raton = (pos_raton[0] + dx, pos_raton[1] + dy)
            if 0 <= nuevo_raton[0] < 10 and 0 <= nuevo_raton[1] < 10:
                valor, _ = minimax(nuevo_raton, pos_gato, pos_queso, profundidad - 1, False)
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_mov = nuevo_raton
        return mejor_valor, mejor_mov
    else:
        peor_valor = float('inf')
        for dx, dy in movimientos:
            nuevo_gato = (pos_gato[0] + dx, pos_gato[1] + dy)
            if 0 <= nuevo_gato[0] < 10 and 0 <= nuevo_gato[1] < 10:
                valor, _ = minimax(pos_raton, nuevo_gato, pos_queso, profundidad - 1, True)
                if valor < peor_valor:
                    peor_valor = valor
        return peor_valor, pos_raton


def mostrar_tablero(tablero):
    for fila in tablero:
        print(''.join(fila))
    print()


def mover_gato(posicion_gato):
    columna, fila = posicion_gato
    opcion = input('seleccioná una opción de movimiento (w/a/s/d): ')
    if opcion == "w":
        nueva_posicion = (columna - 1, fila)
    elif opcion == "s":
        nueva_posicion = (columna + 1, fila)
    elif opcion == "a":
        nueva_posicion = (columna, fila - 1)
    elif opcion == "d":
        nueva_posicion = (columna, fila + 1)
    else:
        print('opción no válida, perdiste tu turno')
        nueva_posicion = posicion_gato
    if 0 <= nueva_posicion[0] < 10 and 0 <= nueva_posicion[1] < 10:
        return nueva_posicion
    else:
        return posicion_gato


def pedir_posicion_gato():
    fila = int(input("Ingresá la fila del gato (0 a 9): "))
    columna = int(input("Ingresá la columna del gato (0 a 9): "))
    if 0 <= fila <= 9 and 0 <= columna <= 9:
        return (columna, fila)
    else:
        print("Posición inválida. Debe estar entre 0 y 9.")
        return pedir_posicion_gato()


def crear_tablero():
    return [["[]" for _ in range(10)] for _ in range(10)]


# --- INICIO DEL JUEGO ---

posicion_gato = pedir_posicion_gato()
posicion_raton = (0, 0)
posicion_queso = (4, 4)

tablero = crear_tablero()
tablero[posicion_gato[0]][posicion_gato[1]] = "🐈"
tablero[posicion_raton[0]][posicion_raton[1]] = "🐁"
tablero[posicion_queso[0]][posicion_queso[1]] = "🧀"

mostrar_tablero(tablero)

turnos_gato = 0
turnos_raton = 0

while True:
    if posicion_raton == posicion_gato:
        print("¡El gato ganó!")
        break
    elif posicion_raton == posicion_queso:
        print("¡El ratón ganó!")
        break
    elif turnos_gato >= 30 and turnos_raton >= 30:
        print("¡Empate! Se acabaron los turnos.")
        break

    # Turno del ratón
    if turnos_raton < 30:
        tablero[posicion_raton[0]][posicion_raton[1]] = "[]"
        _, posicion_raton = minimax(posicion_raton, posicion_gato, posicion_queso, 8, True)
        tablero[posicion_raton[0]][posicion_raton[1]] = "🐁"
        turnos_raton += 1

    # Turno del gato
    if turnos_gato < 30:
        nueva_posicion_gato = mover_gato(posicion_gato)
        tablero[posicion_gato[0]][posicion_gato[1]] = "[]"
        tablero[posicion_queso[0]][posicion_queso[1]] = "🧀"
        posicion_gato = nueva_posicion_gato
        tablero[posicion_gato[0]][posicion_gato[1]] = "🐈"
        turnos_gato += 1

    mostrar_tablero(tablero)
