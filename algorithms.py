import math
from node import Node, possible_moves, get_player, get_heuristic_value, is_terminal, ai_make_move


def min_max(node: Node, depth: int = 0, max_depth: int = None) -> int:
    """ Determines the optimal move for a player using the Minimax algorithm """
    if max_depth is None:
        max_depth = get_opt_depth(node)

    if is_terminal(node) or depth == max_depth:
        return get_heuristic_value(node)
    
    best_move = None
    player = get_player(node)

    if player == 1:  # Minimizing player
        min_eval = math.inf
        for move in possible_moves(node):  # Iterate over all possible moves from the current state
            new_node, _ = ai_make_move(node, move)
            eval = min_max(new_node, depth=depth+1, max_depth=max_depth)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return best_move if depth == 0 else min_eval  # Return move at root, else return evaluation

    else:  # Maximizing player
        max_eval = -math.inf
        for move in possible_moves(node):  # Iterate over all possible moves from the current state
            new_node, _ = ai_make_move(node, move)
            eval = min_max(new_node, depth=depth+1, max_depth=max_depth)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move if depth == 0 else max_eval  # Return move at root, else return evaluation


def alpha_beta(node: Node, depth: int = 0, max_depth: int = None, alpha: float = -math.inf, beta: float = math.inf) -> int:
    """ Determines the optimal move for a player using the Alpha-Beta pruning algorithm """
    # alpha: best score that the maximizer can guarantee so far.
    # beta: best score that the minimizer can guarantee so far.

    if max_depth is None:
        max_depth = get_opt_depth(node)

    if is_terminal(node) or depth == max_depth:
        return get_heuristic_value(node)
    
    best_move = None
    player = get_player(node)

    if player == 1:  # Minimizing player
        min_eval = math.inf
        for move in possible_moves(node):  # Iterate over all possible moves from the current state
            new_node, _ = ai_make_move(node, move)
            eval = alpha_beta(new_node, depth=depth+1, max_depth=max_depth, alpha=alpha, beta=beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return best_move if depth == 0 else min_eval  # Return move at root, else return evaluation

    else:  # Maximizing player
        max_eval = -math.inf
        for move in possible_moves(node):  # Iterate over all possible moves from the current state
            new_node, _ = ai_make_move(node, move)
            eval = alpha_beta(new_node, depth=depth+1, max_depth=max_depth, alpha=alpha, beta=beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return best_move if depth == 0 else max_eval  # Return move at root, else return evaluation


def get_opt_depth(node: Node) -> int:
    """ Automatically selects a suitable maximum depth for the algorithm to balance performance and quality """
    length = len(node.sequence)

    if length > 22:
        return 7
    elif length > 16:
        return 8
    elif length > 12:
        return 9
    else:
        return 10
