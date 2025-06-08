 #funcion para condicionar puntuacion al raton
def puntuar_estado(posicion_raton, posicion_gato, turno):
    if posicion_gato == posicion_raton:
        return -1000
    if turno >= max_turnos:
        return +1000
    #distancia manhatan
    distancia_al_gato = abs(posicion_raton[0] - posicion_gato[0]) + abs(posicion_raton[1] - posicion_gato[1])
    return distancia_al_gato
 


movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#funcion para optener los movimientos posibes del raton
def obtener_pos_movimientos(posicion_actual):
    movimientos_pos = []
    for direccion in movimientos:
        nueva_pos = (posicion_actual[0] + direccion[0], posicion_actual[1] + direccion[1])
        if 0 <= nueva_pos[0] < 10 and 0 <= nueva_pos[1] < 10:
            movimientos_pos.append(nueva_pos)
    return movimientos_pos

# funcion para implementar el algoritmo minimax
def minimax(pos_raton, pos_gato, profundidad, maximizador, turno):
    if profundidad == 0 or pos_raton == pos_gato:
        return None, puntuar_estado(pos_raton, pos_gato, turno)

    if maximizador:
        mejor_valor = float('-inf')
        mejor_mov = pos_raton
        for nueva_pos in obtener_pos_movimientos(pos_raton):
            _, valor = minimax(nueva_pos, pos_gato, profundidad - 1, False, turno + 1)
            if valor > mejor_valor: 
                mejor_valor = valor
                mejor_mov = nueva_pos
        return mejor_mov, mejor_valor
    else:
        peor_valor = float('inf')
        peor_mov = pos_gato
        for nueva_pos in obtener_pos_movimientos(pos_gato):
            _, valor = minimax(pos_raton, nueva_pos, profundidad - 1, True, turno + 1)
            if valor < peor_valor:
                peor_valor = valor
                peor_mov = nueva_pos
        return peor_mov, peor_valor
    
#funcion para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(''.join(fila))
    print()
# esta funcion define las condiciones de los movimientos del gato
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

#creacion del tablero
dimension= 10
def crear_tablero():
    return [["[]" for _ in range(dimension)] for _ in range(dimension)]
 

# esta funcion sirve para que el gato no se mueva fuera del tablero
'''def puntuar_estado(posicion_raton, posicion_gato, turno):
    if posicion_gato == posicion_raton:
        return -1000
    if turno >= max_turnos:
        return +1000
    #distancia manhatan
    distancia_al_gato = abs(posicion_raton[0] - posicion_gato[0]) + abs(posicion_raton[1] - posicion_gato[1])
    return distancia_al_gato'''


# Posiciones iniciales
posicion_gato = (9,9)
posicion_raton = (0, 0)

tablero = crear_tablero()
tablero[posicion_gato[0]][posicion_gato[1]] = "🐈"
tablero[posicion_raton[0]][posicion_raton[1]] = "🐁"

max_turnos = 30
turno = 0
mostrar_tablero(tablero)

# Bucle del juego
while True:
    if posicion_raton == posicion_gato:
        print("¡El gato ganó!")
        tablero[posicion_gato[0]][posicion_gato[1]]= "👻"
        mostrar_tablero(tablero)
        break
    elif turno >= max_turnos:
        print("¡El ratón escapó! Perdiste.")
        mostrar_tablero(tablero)
        break

    # Turno del ratón (usa minimax)
    tablero[posicion_raton[0]][posicion_raton[1]] = "[]"
    nueva_pos_raton, _ = minimax(posicion_raton, posicion_gato, 8, True, turno)
    posicion_raton = nueva_pos_raton
    tablero[posicion_raton[0]][posicion_raton[1]] = "🐁"
    mostrar_tablero(tablero)

    # Turno del gato (jugador)
    nueva_posicion_gato = mover_gato(posicion_gato)
    tablero[posicion_gato[0]][posicion_gato[1]] = "[]"
    posicion_gato = nueva_posicion_gato
    tablero[posicion_gato[0]][posicion_gato[1]] = "🐈" 
    mostrar_tablero(tablero)

    #se suma un turno
    turno += 1
