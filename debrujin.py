from collections import defaultdict
import random


class DeBruijnGraph():
    """Main class for De Bruijn graphs

    Private Attributes:
        graph (defaultdict of lists): Edges for De Bruijn graph
        first_node (str): starting position for traversing the graph
    """

    def __init__(self, input_string, k):
        self.graph = defaultdict(list)
        self.first_node = ''
        self.build_debruijn_graph(input_string, k)

    def add_edge(self, left, right):
        ''' This function adds a new edge to the graph

        Args:
            left (str): The k-1 mer for the left edge
            right (str): The k-1 mer for the right edge

        Updates graph attribute to add right to the list named left in defaultdict
        '''
        pass

    def remove_edge(self, left, right):
        ''' This function removes an edge from the graph

        Args:
            left (str): The k-1 mer for the left edge
            right (str): The k-1 mer for the right edge

        Updates graph attribute to remove right from the list named left in defaultdict
        '''
        pass

    def build_debruijn_graph(self, input_string, k):
        ''' This function builds a De Buijn graph from a string

        Args:
            input_string (str): string to use for building the graph
            k (int): k-mer length for graph construction

        Updates graph attribute to add all valid edges from the string

        Example:
        >>> dbg = DeBruijnGraph("this this this is a test", 4)
        >>> print(dbg.graph) #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        defaultdict(<class 'list'>, {'thi': ['his', 'his', 'his'], 'his': ['is ', 'is ', 'is '], ...)
        '''
        nodes = k - 1
        word_assembly = input_string.split()
        edge_num = len(word_assembly) - k + 1

        for i in range(len(nodes)):
            # iterates through the character with the number of nodes left and right
            assem_kmer = input_string[i:i + k]
            left_assem = assem_kmer[:-1]
            right_assem = assem_kmer[1:]
        return left_assem, right_assem


graph = DeBruijnGraph("fool me once shame on shame on you fool me", 6)
print(graph.graph)

import doctest
doctest.testmod()

# expected value

"""
Expected output:
defaultdict(<class 'list'>, {'fool ': ['ool m', 'ool m'], 'ool m': ['ol me', 'ol me'], 'ol me': ['l me '], 'l me ': [' me o'], ' me o': ['me on'], 'me on': ['e onc', 'e on ', 'e on '], 'e onc': [' once'], ' once': ['once '], 'once ': ['nce s'], 'nce s': ['ce sh'], 'ce sh': ['e sha'], 'e sha': [' sham'], ' sham': ['shame', 'shame'], 'shame': ['hame ', 'hame '], 'hame ': ['ame o', 'ame o'], 'ame o': ['me on', 'me on'], 'e on ': [' on s', ' on y'], ' on s': ['on sh'], 'on sh': ['n sha'], 'n sha': [' sham'], ' on y': ['on yo'], 'on yo': ['n you'], 'n you': [' you '], ' you ': ['you f'], 'you f': ['ou fo'], 'ou fo': ['u foo'], 'u foo': [' fool'], ' fool': ['fool ']})"""
