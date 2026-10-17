"""
Reto adicional 17: Tres en raya con Minimax.
El jugador humano utiliza X y la computadora utiliza O.
"""
from typing import Optional
Board = list[str]
def crear_tablero() -> Board:
    """Crea un tablero vacío de nueve casillas."""
    return [" "] * 9
def mostrar_tablero(tablero: Board) -> None:
    """Muestra el tablero numerado para facilitar las jugadas."""
    for fila in range(3):
        inicio = fila * 3
        print(f" {tablero[inicio]} | {tablero[inicio + 1]} | {tablero[inicio + 2]} ")
        if fila < 2:
            print("---+---+---")
def obtener_ganador(tablero: Board) -> Optional[str]:
    """Devuelve X u O si hay ganador, o None si todavía no lo hay."""
    combinaciones = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    for a, b, c in combinaciones:
        if tablero[a] != " " and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    return None
def hay_empate(tablero: Board) -> bool:
    """Comprueba si el tablero está lleno y no hay ganador."""
    return obtener_ganador(tablero) is None and " " not in tablero
def minimax(tablero: Board, turno_computadora: bool) -> int:
    """Evalúa los posibles resultados usando Minimax."""
    ganador = obtener_ganador(tablero)
    if ganador == "O":
        return 1
    if ganador == "X":
        return -1
    if hay_empate(tablero):
        return 0
    if turno_computadora:
        mejor_valor = -2
        for posicion in range(9):
            if tablero[posicion] == " ":
                tablero[posicion] = "O"
                valor = minimax(tablero, False)
                tablero[posicion] = " "
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    mejor_valor = 2
    for posicion in range(9):
        if tablero[posicion] == " ":
            tablero[posicion] = "X"
            valor = minimax(tablero, True)
            tablero[posicion] = " "
            mejor_valor = min(mejor_valor, valor)

    return mejor_valor
def mejor_movimiento(tablero: Board) -> int:
    """Selecciona la casilla con el mejor resultado para la computadora."""
    mejor_valor = -2
    mejor_posicion = -1
    for posicion in range(9):
        if tablero[posicion] == " ":
            tablero[posicion] = "O"
            valor = minimax(tablero, False)
            tablero[posicion] = " "
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_posicion = posicion
    return mejor_posicion
def jugar() -> None:
    """Ejecuta una partida interactiva en la consola."""
    tablero = crear_tablero()
    print("=== TRES EN RAYA ===")
    print("Tú eres X y la computadora es O.")
    print("Elige una posición del 1 al 9:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()
    while True:
        try:
            posicion = int(input("Tu movimiento (1-9): ")) - 1
        except ValueError:
            print("Introduce un número del 1 al 9.")
            continue
        if posicion < 0 or posicion > 8 or tablero[posicion] != " ":
            print("Casilla no válida u ocupada. Intenta otra vez.")
            continue
        tablero[posicion] = "X"
        print("\nTu jugada:")
        mostrar_tablero(tablero)
        if obtener_ganador(tablero) == "X":
            print("¡Ganaste!")
            break
        if hay_empate(tablero):
            print("¡Empate!")
            break
        movimiento = mejor_movimiento(tablero)
        tablero[movimiento] = "O"
        print("\nMovimiento de la computadora (Minimax):")
        mostrar_tablero(tablero)
        if obtener_ganador(tablero) == "O":
            print("La computadora ganó.")
            break
        if hay_empate(tablero):
            print("¡Empate!")
            break
if __name__ == "__main__":
    jugar()
