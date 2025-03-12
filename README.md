# Project 7 Burrows-Wheeler Transform (BWT)
## Description 

The Burrows-Wheeler Transform (BWT) is an algorithm for data compression allowing low computational storage and easy access. The algorithm first sorts rotational possibility of the characters then organized them lexicographically and then grabs the last column. Now in bioinformatics it is an efficient method to query matching alignments to the reference genome. In this program we implemented the BWT algorithm for string so users may query portions of the string for a match using the moving window algorithm from the compressed data.

## Pertinent documentation and usage write-up
- Python ver 3.13
- Package: Collection
Run the program with a Python IDE.

## Pseudocode
BWT algorithm first starts with a string assembly that is rotated using the $ as the marker. Consider the syntax of string assembly using the indexing and find the method to sort the different rotations lexigraphically. Perhaps find a list of the lexigraphic orders or package. To make a suffix array based on the string mak a for loop from the number of characters in the string to iterate for the position based on the sorted strings. For suffix assembly use a for loop to go over the list of numbers and index to find the BWT text. For the calculate count function the implementation idea was to use the Counter function then sort after initializing the dictionary. Setting the first result to 0 is important to adding the counts afterward using variables. For calculate occurance function would be to first get the dictionary of the unique value to put in the number of lists until the recognized unique character is matched. The update range function would need the upper and lower with indexing. For the find_math assembling everything together would need to convert the inputs of the suffix, int array, and bwt_string to find match_pos. We were unsure how everything assembles and interacts with one another or how the calculate occurance and update range function comes together so more reading is required.
## Reflection 
There was difficulty interpreting the output for `cal_occur` function as the example output was `cal_occur('annb$aa')
        {'$': [0, 0, 0, 0, 1, 1, 1], 'a': [0, 1, 1, 1, 1, 2, 3], 'b': [0, 0, 0, 1, 1, 1, 1], 'n': [0, 0, 2, 2, 2, 2, 2]}` when the actual output should be `cal_occur('annb$aa')
        {'$': [0, 0, 0, 0, 1, 1, 1], 'a': [1, 1, 1, 1, 1, 2, 3], 'b': [0, 0, 0, 1, 1, 1, 1], 'n': [0, 1, 2, 2, 2, 2, 2]}
`. After discussing we realized there is an error in the pseudocode and based it off the first example given. We also had trouble assembling everything together as even after we used the function it didn't match the output. 
    
## Appendix
- Burrows, M., & Wheeler, D. J. (1994). A block-sorting lossless data compression algorithm (SRC Research Report No. 124). Systems Research Center.

- Kingsford, C. (n.d.). Burrows-Wheeler Transform. Carnegie Mellon University. Retrieved from https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/bwt.pd
