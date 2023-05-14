import pytest
import kcol_graph_gen


# Invalid Arguments to Generator
def test_invalid_args_generator():
    generator = kcol_graph_gen.KColorableGraphGenerator()
    # Invalid n
    for n_val in [None, "str", -3, -3.4, 3.5]:
        with pytest.raises(
            ValueError, match=r"n must be an integer greater than 0."
        ):
            generator.generate(n_val, 2, 0.2)
    # Invalid k
    for k_val in [None, "str", -3, -3.4, 3.5]:
        with pytest.raises(
            ValueError, match=r"k must be an integer greater than 0."
        ):
            generator.generate(2, k_val, 0.2)
    # Invalid p
    for p_val in [1, 2, -3, "str", None]:
        with pytest.raises(ValueError, match=r"p must be a float."):
            generator.generate(4, 2, p_val)
    # k > n
    with pytest.raises(ValueError, match=r"k must not be greater than n."):
        generator.generate(3, 4)
    # Out of range p
    for p_val in [-1.5, -3.0, 1.1, 1.01]:
        with pytest.raises(
            ValueError, match=r"p must be in the range \[0.0, 1.0\]."
        ):
            generator.generate(4, 2, p_val)


def test_generator_bipartite():
    # with p=0.5
    generator = kcol_graph_gen.KColorableGraphGenerator(42)
    assert generator.generate(4, 2) == [(2, 3), (2, 4), (1, 2)]
    # fully connected bipartite with p=1.0
    generator = kcol_graph_gen.KColorableGraphGenerator(21)
    assert generator.generate(4, 2, 1.0) == [(2, 3), (1, 2), (3, 4), (1, 4)]
