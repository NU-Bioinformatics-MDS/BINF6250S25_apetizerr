from collections import defaultdict
import random


class DeBruijnGraph:
    """Main class for De Bruijn graphs

    Private Attributes:
        graph (defaultdict of lists): Edges for De Bruijn graph
        first_node (str): starting position for traversing the graph
    """

    def __init__(self, input_string, k):
        self.graph = defaultdict(list)
        self.first_node = ""
        self.build_debruijn_graph(input_string, k)

    def add_edge(self, left, right):
        """This function adds a new edge to the graph

        Args:
            left (str): The k-1 mer for the left edge
            right (str): The k-1 mer for the right edge

        Updates graph attribute to add right to the list named left in defaultdict
        """

    def remove_edge(self, left, right):
        """This function removes an edge from the graph

        Args:
            left (str): The k-1 mer for the left edge
            right (str): The k-1 mer for the right edge

        Updates graph attribute to remove right from the list named left in defaultdict
        """
        pass

    def build_debruijn_graph(self, input_string, k):
        """This function builds a De Buijn graph from a string

        Args:
            input_string (str): string to use for building the graph
            k (int): k-mer length for graph construction

        Updates graph attribute to add all valid edges from the string

        Example:
        >>> dbg = DeBruijnGraph("this this this is a test", 4)
        >>> print(dbg.graph) #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        defaultdict(<class 'list'>, {'thi': ['his', 'his', 'his'], 'his': ['is ', 'is ', 'is '], ...)
        """
        char_pos = 6                                            # start at the chartacter position where the first kmer ends
        self.first_node = input_string[0:5]                     # store this for the Eulerian walk
        while char_pos <= len(input_string):
            prefix = input_string[(char_pos-6):(char_pos-1)]    # this is left
            suffix = input_string[char_pos-5:char_pos]          # this is right
            self.graph[prefix].append(suffix)  # adding prefix and suffix to defaultdict

            char_pos += 1
        print(self.first_node)


graph = DeBruijnGraph("fool me once shame on shame on you fool me", 6)
print(graph.graph)
