"""
Data structure for game states and corresponding functions
"""

import random
from typing import List
from copy import deepcopy

class Node:
    def __init__(self, length: int = 15, first_player_points: int = 100, second_player_points: int = 100, sequence: List[int] = None):
        """ Class constructor """
        self.first_player_points: int = first_player_points
        self.second_player_points: int = second_player_points
        self.sequence: List[int] = sequence if sequence is not None else self.generate_sequence(length)
        self.length = length

    def generate_sequence(self, length: int) -> List[int]:
        """ Generates a random sequence of numbers (from 1 to 4) """
        return [random.randint(1, 4) for _ in range(length)]


def possible_moves(node: Node) -> List[int]:
    """ Returns all possible moves """
    return list(set(node.sequence))  # Returns unique moves (based on value, not position)


def get_player(node: Node) -> int:
    """ Determines the current player """
    return ((node.length - len(node.sequence)) % 2) + 1  # 1 = first, 2 = second


def is_terminal(node: Node) -> bool:
    """ Checks if the game is over """
    return len(node.sequence) == 0


def get_heuristic_value(node: Node) -> int:
    """ Heuristic function with future move simulation """
    sequence = node.sequence[:]
    first_player_points = node.first_player_points
    second_player_points = node.second_player_points
    player = get_player(node)  # 1 = first, 2 = second

    move_cost = {
        1: -1,   # gives 1 point to opponent = removes 1 from self
        2: -4,   # removes 4 points from self
        3: -3,   # gives 3 points to opponent = removes 3 from self
        4: -8    # removes 8 points from self
    }

    """
    Simulates how the game might play out to the end, assuming each player
    chooses the most damaging move for themselves on each turn.
    """
    while sequence:
        best_move = min(sequence, key=lambda x: move_cost[x])
        sequence.remove(best_move)

        if player == 1:  # First player
            first_player_points += move_cost[best_move]
            player += 1
        else:  # Second player
            second_player_points += move_cost[best_move]
            player -= 1

    return first_player_points - second_player_points


def get_winner(node: Node) -> int:
    """ Determines the winner (1, 2 or draw = 0) """
    if node.first_player_points < node.second_player_points:
        return 1
    elif node.first_player_points > node.second_player_points:
        return 2
    else:
        return 0


def update_points(node: Node, player: int, move: int) -> Node:
    """
    Updates points based on move and player.
    - Odd: opponent gains points.
    - Even: player loses double points.
    """
    if player == 1:
        if move % 2 == 0:
            node.first_player_points -= (move * 2)
        else:
            node.second_player_points += move
    else:
        if move % 2 == 0:
            node.second_player_points -= (move * 2)
        else:
            node.first_player_points += move
    return node


def player_make_move(node: Node, place: int) -> Node:
    """ Processes a human move (by index) and updates points """
    player = get_player(node)
    new_node = deepcopy(node)

    if 0 <= place < len(new_node.sequence):
        move = new_node.sequence.pop(place)
    else:
        raise ValueError("`Place` is out of range")

    new_node = update_points(new_node, player, move)

    return new_node


def ai_make_move(node: Node, move: int) -> tuple[Node, int]:
    """
    Processes an AI move: removes the specified `move` value from the sequence,
    choosing a random index if multiple values match.
    """
    player = get_player(node)
    new_node = deepcopy(node)  # Create a copy of the current node to avoid changing the original state

    # Get all indices where the value matches the move
    places = [index for index, value in enumerate(node.sequence) if value == move]
    if places:
        place = random.choice(places)       # Choose a random index from the list
        new_node.sequence.pop(place)        # Remove the move from the sequence
    else:
        raise ValueError("Move is not possible")

    new_node = update_points(new_node, player, move)  # Update points according to the move and player

    return new_node, place  # Return the new node and the index of the move
