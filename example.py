from kcol_graph_gen import KColorableGraphGenerator

generator = KColorableGraphGenerator(seed=42)
edges = generator.generate(4, 2, 0.3)  # Create a bipartite graph

print(edges)  # Printing the list of edges
# > [(2, 3), (2, 4), (1, 2)]

edges = generator.generate(
    6, 3, 0.9
)  # Create a 3-colorable dense graph with 6 vertices

print(edges)  # Printing the list of edges
# > [(2, 4), (1, 2), (3, 4), (1, 5), (2, 3), (4, 5), (2, 6), (5, 6), (3, 6), (2, 5), (1, 3)]
