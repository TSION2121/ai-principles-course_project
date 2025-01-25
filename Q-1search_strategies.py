from collections import deque  # Import deque for BFS queue

# Adjacency dictionary representing the state space graph
adjacency_dict = {
    "Axum": ["Shire", "Adwa"],
    "Adwa": ["Axum", "Adigrat", "Mekelle"],
    "Adigrat": ["Adwa", "Mekelle", "Asmera"],
    "Shire": ["Axum", "Humera", "Debark"],
    "Humera": ["Shire", "Kartum","Gondar"],
    "Kartum": ["Humera", "Metema"],
    "Metema":[ "Gondar","Azezo"],
    "Debark": ["Shire", "Gondar","Metema","Azezo" ],
    "Gondar": ["Debark", "Bahir Dar"],
    "Bahir Dar": ["Gondar", "Debre Markos"],
    "Debre Markos": ["Bahir Dar", "Debre Sina"],
    "Debre Sina": ["Debre Markos", "Lalibela"],
    "Lalibela": ["Debre Sina", "Sekota"],
    "Sekota": ["Lalibela", "Mekelle"],
    "Mekelle": ["Adigrat", "Sekota"],
    "Addis Ababa": ["Debre Birhan", "Ambo", "Adama"],
    "Debre Birhan": ["Debre Sina", "Addis Ababa"],
    "Ambo": ["Addis Ababa", "Nekemte"],
    "Nekemte": ["Ambo", "Gimbi"],
    "Gimbi": ["Nekemte", "Assosa"],
    "Assosa": ["Gimbi"],
    "Adama": ["Addis Ababa", "Batu", "Asella"],
    "Asella": ["Adama", "Dodola"],
    "Dodola": ["Asella", "Bale"],
    "Bale": ["Dodola", "Goba"],
    "Goba": ["Bale", "Sof Oumer"],
    "Sof Oumer": ["Goba"],
    "Batu": ["Adama", "Buta Jira"],
    "Buta Jira": ["Batu", "Hossana"],
    "Hossana": ["Buta Jira", "Wolaita Sodo"],
    "Wolaita Sodo": ["Hossana", "Arba Minch"],
    "Arba Minch": ["Wolaita Sodo", "Konso"],
    "Konso": ["Arba Minch", "Yabelo"],
    "Yabelo": ["Konso", "Moyale"],
    "Moyale": ["Yabelo"],
    "Gore": ["Tepi"],
    "Tepi": ["Gore", "Mizan Teferi"],
    "Mizan Teferi": ["Tepi", "Bonga"],
    "Bonga": ["Mizan Teferi", "Jimma"],
    "Jimma": ["Bonga", "Woliso"],
    "Woliso": ["Jimma", "Ambo"],
    "Finote Selam": ["Bahir Dar"],
    "Gambela": ["Assosa"]
}

class SearchStrategies:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state

    def bfs(self):
        """
        Performs Breadth-First Search (BFS) to find the shortest path from the initial state to the goal state.

        Returns:
        tuple: The path from the initial state to the goal state and the maximum breadth reached.
        """
        visited = set()  # A set to keep track of visited nodes
        queue = deque([(self.initial_state, 0)])  # Initialize the queue with the initial state and depth 0
        parent = {self.initial_state: None}  # A dictionary to track the parent of each node
        max_breadth = 0

        while queue:
            node, depth = queue.popleft()  # Dequeue the first node and its depth
            max_breadth = max(max_breadth, depth)

            if node == self.goal_state:
                return self.construct_path(parent), max_breadth  # If the goal state is found, construct and return the path

            if node not in visited:
                visited.add(node)  # Mark the node as visited
                for neighbor in self.graph.get(node, []):  # Get neighbors from adjacency dictionary
                    if neighbor not in visited:
                        parent[neighbor] = node  # Set the parent of the neighbor to the current node
                        queue.append((neighbor, depth + 1))  # Enqueue the neighbor with updated depth
        return [], max_breadth

    def dfs(self):
        """
        Performs Depth-First Search (DFS) to explore the graph from the initial state to the goal state.

        Returns:
        tuple: The path from the initial state to the goal state and the maximum depth reached.
        """
        visited = set()  # A set to keep track of visited nodes
        stack = [(self.initial_state, 0)]  # Initialize the stack with the initial state and depth 0
        parent = {self.initial_state: None}  # A dictionary to track the parent of each node
        max_depth = 0

        while stack:
            node, depth = stack.pop()  # Pop the last node and its depth from the stack
            max_depth = max(max_depth, depth)

            if node == self.goal_state:
                return self.construct_path(parent), max_depth  # If the goal state is found, construct and return the path

            if node not in visited:
                visited.add(node)  # Mark the node as visited
                for neighbor in self.graph.get(node, []):  # Get neighbors from adjacency dictionary
                    if neighbor not in visited:
                        parent[neighbor] = node  # Set the parent of the neighbor to the current node
                        stack.append((neighbor, depth + 1))  # Push the neighbor with updated depth onto the stack
        return [], max_depth

    def construct_path(self, parent):
        """
        Constructs the path from the initial state to the goal state using the parent dictionary.

        Args:
        parent (dict): A dictionary mapping each node to its parent.

        Returns:
        list: The path from the initial state to the goal state.
        """
        path = []
        node = self.goal_state
        while node:
            path.append(node)  # Append the node to the path
            node = parent[node]  # Move to the parent node
        return path[::-1]  # Reverse the path to get it from initial state to goal state

if __name__ == "__main__":
    # Test 1: From 'Addis Ababa' to 'Moyale'
    search1 = SearchStrategies(adjacency_dict, 'Addis Ababa', 'Moyale')
    bfs_path1, bfs_breadth1 = search1.bfs()
    dfs_path1, dfs_depth1 = search1.dfs()
    print("BFS Path 1:", bfs_path1, "Max Breadth 1:", bfs_breadth1)
    print("DFS Path 1:", dfs_path1, "Max Depth 1:", dfs_depth1)

    # Test 2: From 'Debark' to 'Jimma'
    search2 = SearchStrategies(adjacency_dict, 'Debark', 'Jimma')
    bfs_path2, bfs_breadth2 = search2.bfs()
    dfs_path2, dfs_depth2 = search2.dfs()
    print("BFS Path 2:", bfs_path2, "Max Breadth 2:", bfs_breadth2)
    print("DFS Path 2:", dfs_path2, "Max Depth 2:", dfs_depth2)

    # Test 3: From 'Mizan Teferi' to 'Adwa'
    search3 = SearchStrategies(adjacency_dict, 'Mizan Teferi', 'Adwa')
    bfs_path3, bfs_breadth3 = search3.bfs()
    dfs_path3, dfs_depth3 = search3.dfs()
    print("BFS Path 3:", bfs_path3, "Max Breadth 3:", bfs_breadth3)
    print("DFS Path 3:", dfs_path3, "Max Depth 3:", dfs_depth3)

    # Test 4: From 'Lalibela' to 'Asella'
    search4 = SearchStrategies(adjacency_dict, 'Lalibela', 'Asella')
    bfs_path4, bfs_breadth4 = search4.bfs()
    dfs_path4, dfs_depth4 = search4.dfs()
    print("BFS Path 4:", bfs_path4, "Max Breadth 4:", bfs_breadth4)
    print("DFS Path 4:", dfs_path4, "Max Depth 4:", dfs_depth4)

    search5 = SearchStrategies(adjacency_dict, 'Axum', 'Goba')
    bfs_path5, bfs_breadth5 = search5.bfs()
    dfs_path5, dfs_depth5 = search5.dfs()
    print("BFS Path 5:", bfs_path5, "Max Breadth 5:", bfs_breadth5)
    print("DFS Path 5:", dfs_path5, "Max Depth 5:", dfs_depth5)

    search6 = SearchStrategies(adjacency_dict, 'Tepi', 'Woliso')
    bfs_path6, bfs_breadth6 = search6.bfs()
    dfs_path6, dfs_depth6 = search6.dfs()
    print("BFS Path 6:", bfs_path6, "Max Breadth 6:", bfs_breadth6)
    print("DFS Path 6:", dfs_path6, "Max Depth 6:", dfs_depth6)
