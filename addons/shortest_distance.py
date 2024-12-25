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

        # Update distances to neighbors
        for neighbor, attrs in graph[current_node].items():
            distance = current_dist + attrs['distance']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances