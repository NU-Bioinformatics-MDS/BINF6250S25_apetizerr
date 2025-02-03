A description of the project
Pertinent documentation and usage write-up
Pseudocode
Reflection narrative that describes what went right, what went wrong, what didn't you understand, how it could have been better, and how you could have been better.
Appendix (AI usage, citations, etc.)

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
directed graph: "ba" node  -->  "ban" edge --> "an" edge

-----------------------------------------------------------------------

* "fool me once shame on shame on you fool me" - input string
* {'fool ': ['ool m', 'ool m'], 'ool m': ['ol me', 'ol me'], - beginning of output defaultdict object

* Note: in the output the spaces are ignored in the character count"
<br><br>

#### Given the starting code in the project04.ipynb the following general steps will be needed to complete the task of producing the desired output from the input string<br>
```
    1. Implement add_edge(self, left, right)
    2. Implement remove_edge(self, left, right)
    3. Implement build_debruijn_graph(self, input_string, k)
```