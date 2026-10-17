"""
Implementación del algoritmo Minimax.
"""
from dataclasses import dataclass
from src.game_tree import GameTree
@dataclass
class SearchResult:
    """Guarda el valor encontrado y las hojas evaluadas."""
    value: int
    nodes_evaluated: int


def is_leaf(node: GameTree) -> bool:
    """Comprueba si el nodo es una hoja."""
    return isinstance(node, int)


def minimax(
    node: GameTree,
    maximizing_player: bool = True,
) -> SearchResult:
    """Busca el mejor valor usando Minimax."""
    if is_leaf(node):
        return SearchResult(value=node, nodes_evaluated=1)
    results = [
        minimax(child, not maximizing_player)
        for child in node
    ]
    total_nodes = sum(result.nodes_evaluated for result in results)
    if maximizing_player:
        best_value = max(result.value for result in results)
    else:
        best_value = min(result.value for result in results)
    return SearchResult(
        value=best_value,
        nodes_evaluated=total_nodes,
    )
