# kcol_graph_gen [![Downloads](https://static.pepy.tech/personalized-badge/kcol-graph-gen?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/kcol-graph-gen)

![Cover Logo](https://github.com/imdeep2905/kcol-graph/blob/main/assets/cover.png?raw=true)

_A minimalistic python package to generate a k-colorable graph._

# Installation

Just run `pip install kcol-graph-gen` and you are good to go!

# Usage

Before generating the graph you have to make an object of the class `KColorableGraphGenerator`. You can specify an optional `seed` for the default `random` package which is used during the generation of the graph.

Once the object is crated, you can use `generate` method to generate the graphs. This takes three arguments `n` : number of vertices, `k` : specifying the number of colors, `p(optional, default=0.5)` : Probability with which any edge is added into the graph. Higher the value of `p` denser the resulting graph will be.

Below is the code snippet which demonstrates the usage:

```
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

```
