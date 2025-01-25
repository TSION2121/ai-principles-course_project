import heapq

# Adjacency dictionary representing the state space graph with backward costs
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

def uniform_cost_search(graph, start, goal):
    """
    Perform uniform cost search to find the least-cost path from start to goal.

    Args:
    graph (dict): The state space graph with costs.
    start (str): The initial state.
    goal (str): The goal state.

    Returns:
    list: The path from the start to the goal.
    """
    priority_queue = [(0, start, [])]  # (cost, current_node, path)
    visited = set()  # A set to keep track of visited nodes

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)  # Pop the node with the lowest cost
        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, cost  # Return the path and its cost when the goal is reached

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return None, float('inf')

def customized_uniform_cost_search(graph, start, goals):
    """
    Perform customized uniform cost search to find the least-cost path from start to any of the goal states.

    Args:
    graph (dict): The state space graph with costs.
    start (str): The initial state.
    goals (set): The set of goal states.

    Returns:
    dict: A dictionary with goal states as keys and tuples of (path, cost) as values.
    """
    priority_queue = [(0, start, [])]  # (cost, current_node, path)
    visited = set()  # A set to keep track of visited nodes
    solutions = {}  # A dictionary to store paths and costs for each goal

    while priority_queue and len(goals) > 0:
        cost, node, path = heapq.heappop(priority_queue)  # Pop the node with the lowest cost
        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node in goals:
            solutions[node] = (path, cost)  # Store the solution for the goal
            goals.remove(node)  # Remove the goal from the set

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return solutions

if __name__ == "__main__":
    # Part 2.2: UCS from 'Addis Ababa' to 'Lalibela'
    path, cost = uniform_cost_search(adjacency_dict_costs, 'Addis Ababa', 'Lalibela')
    print("Path to Lalibela:", path, "Cost:", cost)

    # Part 2.3: Customized UCS for multiple goal states
    goals = {"Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"}
    solutions = customized_uniform_cost_search(adjacency_dict_costs, 'Addis Ababa', goals)
    for goal, (path, cost) in solutions.items():
        print(f"Path to {goal}:", path, "Cost:", cost)
