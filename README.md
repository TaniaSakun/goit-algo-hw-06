# goit-algo-hw-06
The repository for the 6th GoItNeo Basic Algorithms homework

# To run the project please complete the following steps:

pip install -r requirements.txt or pip3 install -r requirements.txt
python main.py or python3 main.py

# Task 1:
A model of the Munich Subway station was built, featuring 8 lines and 162 stations. Notably, Munich's subway system differs from Kyiv's in several aspects. Firstly, Kyiv has only 3 lines, and the transit station varies. For instance, to switch from the red line to the blue line in Kyiv, one needs to travel from Khreshchatyk station to Maidan Nezalezhnosti. In Munich, however, a transit station may serve up to 4 different lines, all with the same name. However, this complexity is addressed in subsequent stages of development.

To prevent confusion, the names of the lines were added to the stations. Stations like Hauptbahnhof and Sendlinger Tor have the highest node counts, as they are central locations. Hauptbahnhof serves as the city's central railway station, while Sendlinger Tor is a historic city gate and the closest station to Munich's old town area. That's why each line includes these stations.

# Task 2:
A path was established from Laimer Platz (U5) to Studentenstadt (U6) using Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms. The results of the algorithms' execution are as follows:

# DFS Path:
The DFS path winds through various stations across lines U5, U7, U1, U2, U8, U4, U3, and U6. This path demonstrates the typical behavior of DFS, exploring deeply along certain branches before backtracking. It traverses stations that may not necessarily represent the shortest path between the start and end points.

# BFS Path:
Contrarily, the BFS path starts at Laimer Platz (U5) and concludes at Studentenstadt (U6). Unlike DFS, BFS explores all neighboring stations at each depth level before progressing to the next level. This systematic approach ensures that BFS typically identifies the shortest path first, focusing on stations closer to the start before venturing farther.

# Conclusion:
The DFS path may not represent the shortest path between the two stations, as it explores deeply along certain branches before backtracking. In contrast, the BFS path guarantees the shortest path by systematically exploring neighboring stations at each depth level. In summary, DFS may yield paths that are not optimal in length, whereas BFS reliably finds the shortest path in terms of stations traversed.

# Task 3
In this task, was developed a script to find the shortest path from the "Hauptbahnhof (U1)" station to all other stations in the Munich metro network. The script utilized Dijkstra's algorithm to efficiently compute these shortest paths. Here are some key observations from the results presented in the Shortest Paths Table:

The shortest path from "Hauptbahnhof (U1)" to itself is simply the station "Hauptbahnhof (U1)" with a path length of 0, which is expected.
For nearby stations on the same line, such as "Stiglmaierplatz (U1)" and "Sendlinger Tor (U1)", the shortest paths have a relatively short path length of 2 and 1, respectively.
Some stations require transferring to other lines to reach the destination. For example, to reach "Hauptbahnhof (U2)" or "Hauptbahnhof (U4)", passengers need to transfer lines once, resulting in a path length of 1.
Longer paths are observed for stations further away or requiring multiple transfers. For instance, reaching "Messestadt West (U2)" or "Garching-Forschungszentrum (U6)" involves multiple transfers and results in longer path lengths of 21 and 28, respectively.
Overall, the script effectively computes the shortest paths from "Hauptbahnhof (U1)" to all other stations in the Munich metro network, providing valuable insights into the network's connectivity and travel distances.