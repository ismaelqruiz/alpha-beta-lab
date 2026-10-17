"""
Pruebas unitarias para Minimax y Poda Alfa-Beta.
"""
from src.game_tree import (
    sample_tree,
    medium_tree,
    ordered_tree_for_pruning,
)
from src.minimax import minimax
from src.alpha_beta import alpha_beta
def test_minimax_sample_tree_returns_expected_value():
    result = minimax(sample_tree())

    assert result.value == 5
    assert result.nodes_evaluated == 4
def test_alpha_beta_sample_tree_returns_same_value_as_minimax():
    tree = sample_tree()
    result_minimax = minimax(tree)
    result_alpha_beta = alpha_beta(tree)
    assert result_alpha_beta.value == result_minimax.value
def test_minimax_medium_tree_returns_expected_value():
    result = minimax(medium_tree())
    assert result.value == 7
def test_alpha_beta_medium_tree_returns_same_value_and_evaluates_fewer_nodes():
    tree = medium_tree()
    result_minimax = minimax(tree)
    result_alpha_beta = alpha_beta(tree)
    assert result_alpha_beta.value == result_minimax.value
    assert result_alpha_beta.nodes_evaluated <= result_minimax.nodes_evaluated
def test_alpha_beta_prunes_branches():
    result = alpha_beta(ordered_tree_for_pruning())
    assert result.value == 8
    assert result.branches_pruned > 0
