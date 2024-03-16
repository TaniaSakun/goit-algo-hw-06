import heapq


def single_source_dijkstra_path(G, source, weight="weight"):
    lengths = {}
    paths = {}

    queue = [(0, source)]
    lengths[source] = 0

    while queue:
        (dist, node) = heapq.heappop(queue)

        for neighbor in G[node]:
            new_dist = dist + G[node][neighbor].get(weight, 1)
            if neighbor not in lengths or new_dist < lengths[neighbor]:
                lengths[neighbor] = new_dist
                paths[neighbor] = paths.get(node, []) + [neighbor]
                heapq.heappush(queue, (new_dist, neighbor))

    return paths
