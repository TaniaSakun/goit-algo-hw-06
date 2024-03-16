import networkx as nx
from data_models import Models


def create_graph():
    # Create a graph
    graph = nx.Graph()

    # Add vertexes (stations) to the graph
    subway_stations = Models.subway_stations
    interchange_connections = Models.interchange_connections

    for line, stations in subway_stations.items():
        for station in stations:
            graph.add_node(f"{station} ({line})")

    for line, stations in subway_stations.items():
        for i in range(len(stations) - 1):
            graph.add_edge(f"{stations[i]} ({line})", f"{stations[i+1]} ({line})")

    graph.add_edges_from(interchange_connections)

    return graph


def add_connecitons(graph):
    # Define colors for each line
    line_colors = {
        "U1": "#51832b",
        "U2": "#c4002d",
        "U3": "#ed6721",
        "U4": "#00ab86",
        "U5": "#be7b00",
        "U6": "#0264af",
        "U7": "purple",
        "U8": "brown",
    }

    interchange_connections = Models.interchange_connections
    unique_stations = set()

    # Iterate through each tuple in interchange_connections
    for connection in interchange_connections:
        # Add both station names to the set
        unique_stations.add(connection[0])
        unique_stations.add(connection[1])

    # Set node sizes for transit stations and line stations
    transit_station_size = 150
    line_station_size = 100

    # Initialize lists to store node sizes and colors
    node_sizes = []
    node_colors = []

    # Iterate over each node in the graph
    for node in graph.nodes():
        # Check if the node is a transit station
        if any(station in node for station in unique_stations):
            node_sizes.append(transit_station_size)
        else:
            node_sizes.append(line_station_size)

        # Get the line color for the node
        for line, color in line_colors.items():
            if f"({line})" in node:
                node_colors.append(color)
                break

    return graph, node_sizes, node_colors
