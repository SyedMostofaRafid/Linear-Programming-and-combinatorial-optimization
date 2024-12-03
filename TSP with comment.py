from itertools import permutations

def calculate_total_cost(graph, cost_per_km, path):
    """
    Calculate the total cost of the path based on the distance and cost per kilometer.
    
    Parameters:
    - graph: Dictionary where keys are vertices and values are dictionaries of neighboring vertices and their distances.
    - cost_per_km: Cost per kilometer.
    - path: List of vertices representing the path.
    
    Returns:
    - Total cost of the path.
    """
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_cost = total_distance * cost_per_km
    return total_cost

def travelling_salesman(graph, cost_per_km, start, end):
    """
    Solve the Traveling Salesman Problem (TSP) for a round-trip route starting at the start vertex and ending at the end vertex.
    
    Parameters:
    - graph: Dictionary where keys are vertices and values are dictionaries of neighboring vertices and their distances.
    - cost_per_km: Cost per kilometer.
    - start: Starting vertex.
    - end: Returning vertex.
    
    Returns:
    - Optimal path and its total cost.
    """
    vertices = list(graph.keys())
    
    if start not in vertices or end not in vertices:
        raise ValueError(f"One or both of the vertices {start} and {end} are not in the graph.")
    
    if start in vertices:
        vertices.remove(start)
    if end in vertices:
        vertices.remove(end)
    
    min_path = None
    min_cost = float('inf')

    for perm in permutations(vertices):
        current_path = [start] + list(perm) + [end]  # Start to permutation end
        current_cost = calculate_total_cost(graph, cost_per_km, current_path)
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path

    return min_path, min_cost

def input_graph():
    """
    Input the graph details from the user.
    
    Returns:
    - graph: Dictionary where keys are vertices and values are dictionaries of neighboring vertices and their distances.
    """
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    vertices = []

    for i in range(num_vertices):
        vertex = input(f"Enter vertex {i + 1}: ")
        vertices.append(vertex)
        graph[vertex] = {}

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            distance = float(input(f"Enter the distance between {vertices[i]} and {vertices[j]} (in km): "))
            graph[vertices[i]][vertices[j]] = distance
            graph[vertices[j]][vertices[i]] = distance

    return graph

print("Find The Optimal Solution For Your Delivery Problem With Rafid")

# Input graph and cost
graph = input_graph()
cost_per_km = float(input("Enter the cost per kilometer: "))
start = input("Enter the starting vertex: ")
end = input("Enter the returning vertex: ")

# Calculate optimal path and cost
try:
    path, cost = travelling_salesman(graph, cost_per_km, start, end)
    print(f"Optimal path from {start} to {end}: {path}")
    print(f"Total cost for the round trip: {cost:.2f}")
except ValueError as e:
    print(e)
