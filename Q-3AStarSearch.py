import heapq

class AStarSearch:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics

    def a_star_search(self, start, goal):
        """
        Perform A* search to find the least-cost path from start to goal.

        Args:
        graph (dict): The state space graph with costs.
        start (str): The initial state.
        goal (str): The goal state.

        Returns:
        tuple: The path from the start to the goal and the total cost.
        """
        priority_queue = [(0 + self.heuristics[start], 0, start, [])]  # (f_score, g_score, current_node, path)
        visited = set()  # A set to keep track of visited nodes

        print(f"{'Node':<12} {'g_score (Backward Cost)':<25} {'Heuristic (h_score)':<20} {'f_score (Total)'}")

        while priority_queue:
            f_score, g_score, node, path = heapq.heappop(priority_queue)  # Pop the node with the lowest f_score
            if node in visited:
                continue

            visited.add(node)
            path = path + [node]

            print(f"{node:<12} {g_score:<25} {self.heuristics[node]:<20} {f_score}")

            if node == goal:
                return path, g_score  # Return the path and its cost when the goal is reached

            for neighbor, cost in self.graph.get(node, []):
                if neighbor not in visited:
                    g = g_score + cost
                    f = g + self.heuristics[neighbor]
                    heapq.heappush(priority_queue, (f, g, neighbor, path))

        return None, float('inf')

    def detailed_path(self, path):
        """
        Provide a detailed breakdown of the path with costs between nodes.

        Args:
        path (list): The path from the start to the goal.

        Returns:
        str: A formatted string with the detailed path and costs.
        """
        detailed_str = "Detailed Path:\n"
        total_cost = 0

        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            for neighbor, cost in self.graph[current_node]:
                if neighbor == next_node:
                    detailed_str += f"{current_node} -> {next_node} (Cost: {cost})\n"
                    total_cost += cost
                    break

        detailed_str += f"Total Cost: {total_cost}"
        return detailed_str

# Example adjacency list with backward costs
adjacency_dict_costs = {
    "Addis Ababa": [("Debre Birhan", 4), ("Ambo", 6), ("Adama", 3)],
    "Debre Birhan": [("Debre Sina", 8), ("Addis Ababa", 4)],
    "Ambo": [("Nekemte", 7), ("Addis Ababa", 6)],
    "Adama": [("Batu", 5), ("Asella", 4), ("Addis Ababa", 3)],
    "Debre Sina": [("Debre Markos", 6), ("Lalibela", 10), ("Debre Birhan", 8)],
    "Debre Markos": [("Bahir Dar", 9), ("Debre Sina", 6)],
    "Lalibela": [("Sekota", 12), ("Debre Sina", 10)],
    "Sekota": [("Mekelle", 7), ("Lalibela", 12)],
    "Mekelle": [("Adigrat", 4), ("Sekota", 7)],
    "Adigrat": [("Adwa", 3), ("Mekelle", 4)],
    "Adwa": [("Axum", 2), ("Adigrat", 3)],
    "Axum": [("Shire", 5), ("Adwa", 2)],
    "Shire": [("Kurmuk", 6), ("Debark", 8), ("Axum", 5)],
    "Kurmuk": [("Kartu", 9), ("Shire", 6)],
    "Kartu": [("Kurmuk", 9)],
    "Debark": [("Gondar", 7), ("Shire", 8)],
    "Gondar": [("Bahir Dar", 5), ("Debark", 7)],
    "Bahir Dar": [("Gondar", 5), ("Debre Markos", 9)],
    "Nekemte": [("Gimbi", 4), ("Ambo", 7)],
    "Gimbi": [("Assosa", 8), ("Nekemte", 4)],
    "Assosa": [("Gimbi", 8)],
    "Batu": [("Buta Jira", 4), ("Adama", 5)],
    "Buta Jira": [("Hossana", 3), ("Batu", 4)],
    "Hossana": [("Wolaita Sodo", 6), ("Buta Jira", 3)],
    "Wolaita Sodo": [("Arba Minch", 7), ("Hossana", 6)],
    "Arba Minch": [("Konso", 5), ("Wolaita Sodo", 7)],
    "Konso": [("Yabelo", 6), ("Arba Minch", 5)],
    "Yabelo": [("Moyale", 4), ("Konso", 6)],
    "Moyale": [("Yabelo", 4)],
    "Gore": [("Tepi", 3)],
    "Tepi": [("Mizan Teferi", 5), ("Gore", 3)],
    "Mizan Teferi": [("Bonga", 6), ("Tepi", 5)],
    "Bonga": [("Jimma", 4), ("Mizan Teferi", 6)],
    "Jimma": [("Woliso", 7), ("Bonga", 4)],
    "Woliso": [("Jimma", 7), ("Ambo", 5)],
    "Bale": [("Goba", 3)],
    "Goba": [("Bale", 3), ("Sof Oumer", 5)],
    "Sof Oumer": [("Goba", 5)]
}

# Example heuristic values for the states (updated to include 'Asella')
heuristics = {
    "Addis Ababa": 10,
    "Debre Birhan": 8,
    "Ambo": 8,
    "Adama": 7,
    "Debre Sina": 6,
    "Debre Markos": 5,
    "Lalibela": 0,  # Goal state
    "Sekota": 3,
    "Mekelle": 4,
    "Adigrat": 5,
    "Adwa": 6,
    "Axum": 7,
    "Shire": 8,
    "Kurmuk": 9,
    "Kartu": 10,
    "Debark": 6,
    "Gondar": 5,
    "Bahir Dar": 4,
    "Nekemte": 7,
    "Gimbi": 8,
    "Assosa": 9,
    "Batu": 6,
    "Buta Jira": 5,
    "Hossana": 4,
    "Wolaita Sodo": 3,
    "Arba Minch": 2,
    "Konso": 1,
    "Yabelo": 1,
    "Moyale": 0,  # Goal state
    "Gore": 8,
    "Tepi": 7,
    "Mizan Teferi": 6,
    "Bonga": 5,
    "Jimma": 4,
    "Woliso": 3,
    "Bale": 4,
    "Goba": 3,
    "Sof Oumer": 2,
    "Asella": 6  # Add the missing heuristic value for Asella
}

# Usage example
search = AStarSearch(adjacency_dict_costs, heuristics)
path, cost = search.a_star_search('Addis Ababa', 'Moyale')
print(f"Path to Moyale: {path}")
print(f"Total Cost: {cost}\n")
print(search.detailed_path(path))
