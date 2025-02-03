# DeBrujin Graph Project

## Description of the project

The program constructs a De Brujin 

## Pertinent documentation and usage write-up

Python ver. 3.11
Package: 

## Psuedocode
Required routines
        * add_edge() - required to build for use with class
        * remove_edge() - required to build for use with class
        * defaultdict - a directed graph.  Each "left" node can have multiple "right" nodes connected to it, forming an adjacency list representation.

*From the notebook file:*
```
build_debruijn_graph:
define substring length k and input string
For each k-length substring of input:
  split k mer into left and right k-1 mer
  add k-1 mers as nodes with a directed edge from left k-1 mer to right k-1 mer
```

*Definitons:*<br>

    mer: Abbreviation for oligomer, a short sequence of any repeating or potentially repeating units, in our case likely a DNA strand.
    kmer: a mer of length k, also referred to as a k-mer or an nmer where the length is designated by n instead of k.  

*What this means:*<br>
    To build the DeBruin Graph step-by-step:
```
    1. Define k and Input: Choose the length of substrings you want to work with (k) and provide the input string (some DNA or RNA sequence).
    2. Extract k-mers: Slide a window of length k across your input string, extracting each k-mer, **these are the edges of the graph**.
    3. Split into (k-1)-mers, **these are the nodes of the graph**: For each k-mer, split it into two overlapping (k-1)-mers:
    4. "left" (k-1)-mer: The first (k-1) characters
    5. "right" (k-1)-mer: The last (k-1) characters
```
#### Example from a short word:  "banana"
k = 3
first mer = "ban"
left k-1 mer = "ba"
right k-1 mer = "an"
directed graph: "ba" node  -->  directed edge connecting the overlap of "ba"+"an" --> "an" node

-----------------------------------------------------------------------

* "fool me once shame on shame on you fool me" - input string
* {'fool ': ['ool m', 'ool m'], 'ool m': ['ol me', 'ol me'], - beginning of output defaultdict object

<br><br>

#### Given the starting code in the project04.ipynb the following general steps will be needed to complete the task of producing the desired output from the input string<br>

1.  Dependecies
    Import and use the standardized defaultdict(list) to allow each new key to have an empty list created as it's value
    Import random

1. Implement add_edge(self, left, right)
```python
Each time a (left) node is encountered:
    Check if it exists as a key, if not:
        Add it to defaultdict as a key.
        Add (right) node to the value object (list).
    If the node does exist as a key:
        Add (right) node to the value object (list). 
```
2. Implement remove_edge(self, left, right)
```python
Each time a (left) node is encountered:
    Check if it exists as a key, if not:
        print("Warning, can't remove, that starting node doesn't exist!")
    If the (left) node does exist as a key:
        Check if the (right) node exists in the list associated with the (left) node.
        If the (right) node exists in the list:
            Remove **one instance** of the (right) node from the list. 
        If the (right) node does not exist:
            print("Warning, can't remove, that ending node doesn't exist!")
```
3. Implement build_debruijn_graph(self, input_string, k)
```python
define substring length k and input string
For each k-length substring of input:
  split k mer into left and right k-1 mer
  add k-1 mers as nodes with a directed edge from left k-1 mer to right k-1 mer
```

4. Define the method to display the graph
```python
@property
def graph(self):
    return self._graph
```

## Appendix:
The resulting script used to create the output for assigment one was informed by the results fo the following propts searches and reference documents.

Website:
    GeeksForGeeks - `https://www.geeksforgeeks.org/de-bruijn-sequence-set-1/?ref=header_outind`
    GeeksForGeeks - `https://www.geeksforgeeks.org/eulerian-path-eulerian-circuit-in-python/?ref=ml_lbp`
    Gemini Pro Prompt   - Does this summarize the key logic for a Debrijn graph?  populate the dict:
                        Each time an input_string is presented:
                            parse the input_string into kmers of len(k)
                            build the (left) node as kmer[:-1] ket in defaultdict
                            build the (right) node as kmer[1:] value in list in defaultdict
                        loop through the keys

                        -  how to bold in markdown language
                        -  how to make an askterisk in markdown?
                        -  Are these required ">>>" when using doctest?
                        -  how to embed a block of code into an md file?




    



