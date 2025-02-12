from collections import defaultdict
import random

class DeBruijnGraph:

    def __init__(self, input_string, k):
        self.graph = defaultdict(list)
        self.first_node = ""
        self.build_debruijn_graph(input_string, k)

    def add_edge(self, left, right):
        ''' This function adds a new edge to the graph
        
        Args:
            left (str): The k-1 mer for the left edge
            right (str): The k-1 mer for the right edge

        Updates graph attribute to add right to the list named left in defaultdict   
        '''
        self.graph[left].append(right)

    def remove_edge(self, left, right):
        ''' This function removes an edge from the graph
        
        Args:
            left (str): The k-1 mer for the left edge
            right (str): The k-1 mer for the right edge

        Updates graph attribute to remove right from the list named left in defaultdict
        '''
        self.graph[left].remove(right)

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
        char_pos = k
        self.first_node = input_string[0 : k - 1]
        while char_pos <= len(input_string):
            prefix = input_string[(char_pos - k) : (char_pos - 1)]
            suffix = input_string[char_pos - k + 1 : char_pos]
            self.add_edge(prefix, suffix)
            char_pos += 1
        # I like the way k was used here in the while loop. So it goes from the k length to the end of the string. Very nice.

    def find_eulerian_path(self):
        """This function searches for a Eulerian path in the debruijn graph by recursively calling a depth first search function."""

        def dfs(node, path):
            """Performs depth first search to find the path."""
            while self.graph[node]:
                random_index = random.randint(0, len(self.graph[node]) - 1) # Chooses a random node index based on the size of the list
                neighbor = self.graph[node][random_index]                   # Retrieves the neighbor identified by random_index
                self.remove_edge(node, neighbor)                            # Removes the right node from the graph eliminating an edge
                dfs(neighbor, path)                                         # Recursively Calls the dfs function with the neighbor node
            path.append(node) 
        # I like this nested DFS search routine - I believe it wanted find_eulerian_path to be recursive,
        # But this kind of fits the way I think about it a little better.
        # However - since you are reversing the path before returning it - it will be reversed from what was expected in the initial comments.
        # Because it is stated in the original comments I would suggest returning the reversed path to match.
        path = []
        dfs(self.first_node, path)  # Start from self.first_node
        return path[::-1]  # Reverse the path since the path is found in reverse order


# Example usage:
graph = DeBruijnGraph("fool me once shame on shame on you fool me", 6)
print("De Bruijn Graph:", graph.graph)
eulerian_path = graph.find_eulerian_path()
print("Eulerian Path:", eulerian_path)
