class Node:
    def __init__(self, name, utility=0, children=None):
        """
        Initialize a node in the graph.

        Args:
        name (str): The name of the node (city).
        utility (int): The utility value of the node (default is 0).
        children (list): The list of child nodes (default is None).
        """
        self.name = name
        self.utility = utility
        self.children = children if children is not None else []

class MiniMaxSearch:
    def __init__(self, root):
        """
        Initialize the MiniMax search with the root node.

        Args:
        root (Node): The root node of the graph.
        """
        self.root = root

    def minimax(self, node, depth, maximizing_player):
        """
        Perform the MiniMax search algorithm.

        Args:
        node (Node): The current node in the search.
        depth (int): The current depth of the search.
        maximizing_player (bool): Whether the current player is maximizing.

        Returns:
        int: The utility value of the node.
        """
        # Base case: if depth is 0 or the node has no children, return the node's utility value
        if depth == 0 or not node.children:
            return node.utility

        # If the current player is maximizing
        if maximizing_player:
            max_eval = float('-inf')
            # Evaluate each child node
            for child in node.children:
                eval = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        # If the current player is minimizing
        else:
            min_eval = float('inf')
            # Evaluate each child node
            for child in node.children:
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self):
        """
        Find the best move for the agent from the root node.

        Returns:
        str: The name of the best achievable destination.
        """
        best_value = float('-inf')
        best_move = None
        # Evaluate each child node of the root
        for child in self.root.children:
            move_value = self.minimax(child, depth=3, maximizing_player=False)
            if move_value > best_value:
                best_value = move_value
                best_move = child
        return best_move.name

# Example usage:
# Define the graph nodes and their connections
addis_ababa = Node("Addis Ababa")
gedo = Node("Gedo", children=[Node("Gimbi", 8), Node("Limu", 8)])
ambo = Node("Ambo", children=[Node("Hossana", 6), Node("Durame", 5)])
adama = Node("Adama", children=[Node("Harar", 10), Node("Chiro", 6)])
addis_ababa.children = [gedo, ambo, adama]

# Initialize the MiniMax search with the root node
search = MiniMaxSearch(addis_ababa)

# Find the best move
best_destination = search.best_move()
print(f"The best achievable destination is: {best_destination}")
