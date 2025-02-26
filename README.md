# Phylogenic Tree Construction Project

## Description
Phylogenic studies undergo evolutionary insights into how organisms evolved over-time. Pretaining to both phenotypes and genotypes, this mapping is used to visualize the distance between many field of studies including drug resistance, evolutionary changes, and population level changes. In this project we constructed an algorithm that pretains to calculate the relations of genetic overlap between SARS-Cov viruses. This project accomplishes this with a combination of both Smith-waterman algorithm and a neighborhood growing tree. Especially in regards to the phylogenic tree, the Smith-Waterman is used to determine the distance between the genetics of Sars-Cov virsuses then calculates the Q matrix joining the neighboring virsus that share an amino acid similarity. The program then visualizes the tree using the Newick format to construct a visual representation and distance between the viruses.

## Documentation
- Run the program using Python ver 3.13
- Data: Organisms with amino acid sequence is used to assemble the tree as the input.
Packages: 
  1. Ensure the typing package has List, Tuple, and Dict.
  2. Ensure the package numpy is installed.
  3. Ensure the package ete3 is installed.

## Pseudocode
Iterate through the sequence file using header and sequence as the dictionary for initializing the genetic data and bind them together into a dictionary. Although the assignment is a familiar in regards to Smith Waterman algorithim implemented previously consider the differences and implication this can have virus amino acid versus nucleotides. Does the algorithm require adjustment or change? Furthermore consider the intent is to find the diverging differences between the genetic to establish branches and leaves rather than pair-wise alignment. How can we develop the nodes for the tree is another consideration needed. Looking up the documentation to use the ete3 package is also needed and the Newick format tree string.

## Reflection 

The biggest challenge was implementing the phylogeny tree for neighbor_joining even after the guidance from class was difficult to apply things in concept to code. Assmebling everything together from the node to the branches while understood conceptually was difficult to translate in code. This is probably due to lack of experience using class to initialize node. The smith-waterman score and read_fasta was a good sanity check as past development lead to quick implementation for these function which showed a good progress. The syntax or packages used besides the ete3 package were abilities we learned previously like numpy array. So in a way this was a project that built upon the skill we already had using it to make phylogenic trees. 

## Appendix (AI usage, citations, etc.)
- Compeau, P., & Pevzner, P. (2018). Bioinformatics algorithms: An active learning approach (3rd ed.). Active Learning Publishers.
  
