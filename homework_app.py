import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

from data_models import Models
from handlers.dijkstra_algorithm import single_source_dijkstra_path
from handlers.subway_builder import create_graph, add_connecitons
from handlers.search_algorithms import bfs, dfs


class Homework:
    def search_algorithms_task():
        graph, node_sizes, node_colors = add_connecitons(create_graph())
        # Searching a path between some vertices using both algorithms
        start_node = "Laimer Platz (U5)"
        end_node = "Studentenstadt (U6)"

        dfs_path = dfs(graph, start_node, end_node)
        bfs_path = bfs(graph, start_node, end_node)

        print("DFS path:", dfs_path)
        print("\n")
        print("BFS path:", bfs_path)
        
    @staticmethod    
    def calculate_total_time(path, time_map):
        total_time = 0
        for i in range(len(path) - 1):
            station1 = path[i]
            station2 = path[i + 1]
            
            if (station1, station2) in time_map:
                total_time += time_map[(station1, station2)]
            elif (station2, station1) in time_map:  
                total_time += time_map[(station2, station1)]

        return total_time

    def build_graph_task():
        graph, node_sizes, node_colors = add_connecitons(create_graph())
        pos = nx.spring_layout(graph, scale=500)

        # Draw the graph with nodes colored by line and sized based on station type
        plt.figure(figsize=(12, 8))
        nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=node_sizes)
        nx.draw_networkx_edges(graph, pos, alpha=0.5)
        nx.draw_networkx_labels(graph, pos, font_size=5)
        plt.title("Munich Subway Network")
        plt.axis("off")
        plt.show()

        # Graph statistics
        print("Amount of lines:", len(Models.subway_stations))
        print("Amount of stations:", graph.number_of_nodes())
        print("Amount of connections:", graph.number_of_edges())
        print(
            "The degree of each vertex (the number of connections emanating from the vertex):"
        )
        degrees = dict(graph.degree())
        for station, degree in degrees.items():
            print(station, ":", degree)

    def print_shortest_path_table(graph):
        # Set the source station as "Hauptbahnhof (U1)"
        source_station = "Hauptbahnhof (U1)"

        # Algorithm to find shortest paths using Dijkstra's algorithm
        shortest_paths = single_source_dijkstra_path(graph, source_station)

        # Creating a table to display the shortest paths
        data = {"Source": [], "Target": [], "Shortest Path": [], "Path Length": [], "Travel Time": []}

        # Populate the table with data
        for target, path in shortest_paths.items():
            path_length = nx.dijkstra_path_length(graph, source_station, target)
            
            data["Source"].append(source_station)
            data["Target"].append(target)
            data["Shortest Path"].append(path)
            data["Path Length"].append(path_length)
            data["Travel Time"].append(
                Homework.calculate_total_time(path, Models.edge_weights
            ))

        # Create a DataFrame from the data
        df = pd.DataFrame(data)

        # Display the DataFrame
        print("\nShortest Paths Table:")
        print(df)

    def shortest_path_task():
        graph, node_sizes, node_colors = add_connecitons(create_graph())
        Homework.print_shortest_path_table(graph)
