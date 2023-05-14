import random
from typing import List


class KColorableGraphGenerator:
    """A class to generate the k-colorable graph."""

    def __init__(self, seed=None) -> None:
        """
        Args
        ----

        seed: int
            Initial seed to initialize the default `random` module.
        """
        if seed:
            random.seed(seed)

    def __validate_generate_args(self, n: int, k: int, p: float) -> None:
        """A"""
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be an integer greater than 0.")
        if not isinstance(k, int) or k <= 0:
            raise ValueError("k must be an integer greater than 0.")
        if k > n:
            raise ValueError("k must not be greater than n.")
        if not isinstance(p, float):
            raise ValueError("p must be a float.")
        if p < 0.0 or p > 1.0:
            raise ValueError("p must be in the range [0.0, 1.0].")

    def generate(self, n: int, k: int, p: float = 0.5) -> List:
        """
        Args
        ----

        n : int
            Number of vertices.
        k : int
            Number of colors. For example, for `k = 2` a bipartite graph will
            be generated.
        p : float
            Probability with which any edge is added into the graph. It is
            Explained more in the README.

        Returns
        -------

        List containing edges of the generated graph.
        """
        self.__validate_generate_args(n, k, p)
        graph = set()
        # Create k groups and add the initial k vertices
        groups = []
        for vertex in range(1, k + 1):
            groups.append([vertex])
        # Distribute [k + 1, n] vertices randomly
        for vertex in range(k + 1, n + 1):
            random.choice(groups).append(vertex)
        for group in groups:
            for u in group:
                # Add at least one edges among the groups
                for other_group in groups:
                    if u not in other_group:
                        v = random.choice(other_group)
                        graph.add((u, v) if u < v else (v, u))
                # Add rest of the edges according to the p
                for other_group in groups:
                    if u not in other_group:
                        for v in other_group:
                            if random.uniform(0, 1) < p:
                                graph.add((u, v) if u < v else (v, u))
        return list(graph)
