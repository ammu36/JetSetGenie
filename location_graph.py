import pandas as pd
import networkx as nx
# from addons import dijkstra
import heapq

def dijkstra(graph, start):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes based on distance
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip if the node has already been visited
        if current_dist > distances[current_node]:
            continue

        # Check if current node has neighbors
        if current_node in graph:
            # Update distances to neighbors
            for neighbor, attrs in graph[current_node].items():
                distance = current_dist + attrs['distance']
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

    return distances


# Step 1: Read the CSV file
edges_df = pd.read_csv('dataset/place_route_map.csv')

# Step 2: Create the graph
G = nx.Graph()

# Step 3: Add edges with distances, road conditions, and railway availability
# Iterate over each row in the DataFrame
for _, row in edges_df.iterrows():
    source = row['source']
    target = row['target']
    distance = row['distance']
    road_conditions = row['road_conditions']
    railway_availability = row['railway_availability']

    # Add nodes if they don't exist
    if not G.has_node(source):
        G.add_node(source)
    if not G.has_node(target):
        G.add_node(target)

    # Add edge with attributes
    G.add_edge(source, target, distance=distance, road_conditions=road_conditions, railway_availability=railway_availability)

# Print nodes and their attributes
print("Nodes and their attributes:")
for node, attributes in G.nodes(data=True):
    print(f"Node: {node}, Attributes: {attributes}")

# Print edges and their attributes
print("\nEdges and their attributes:")
for u, v, attributes in G.edges(data=True):
    print(f"Edge: {u} - {v}, Attributes: {attributes}")

start_node = '101'
distances = dijkstra(G, start_node)
print("Shortest distances from node", start_node, ":", distances)

