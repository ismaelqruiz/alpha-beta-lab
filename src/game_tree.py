
"""
Árboles de decisión para el laboratorio Minimax y Poda Alfa-Beta.
"""

from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]



def sample_tree() -> GameTree:
    """Devuelve el árbol pequeño de ejemplo. Resultado esperado: 5."""
    return [
        [3, 5],
        [5, 9],
    ]



def medium_tree() -> GameTree:
    """Devuelve un árbol mediano para comparar los algoritmos."""
    return [
        [[3, 5], [6, 9]],
        [[1, 2], [0, -1]],
        [[7, 4], [8, 6]],
    ]


def ordered_tree_for_pruning() -> GameTree:
    """Devuelve un árbol preparado para demostrar la poda."""
    return [
        [[10, 9], [8, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]
