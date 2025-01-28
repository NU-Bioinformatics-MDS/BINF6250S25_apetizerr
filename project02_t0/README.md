# BINF6250S25 Project 02 Markcov Chain

## Description 
The program highlights the operations of how a Markov Chain takes acount of the probabilities of the string or text files as input it outputs the potential scentence or scentences provided by the frequency. The Markvoc chain is a mathematical system that takes account of the most recent event to determine the outcome based on transitioning from one event to the other. In bioinformatics this is used to determine biological association to measure statistical significance of genetic data (Gafurov, 2022). 

## Documentation and usage write-up

Python: 1.13
Packages: Numpy

The program will take either a text file or string of words separated by spaces to use the scentence predicting outcome by converting the frequencies of words to numerical values in a dictionary of dictionary (DOD).

## Pseudocode

Iterate over the dictionary of dictionary and read the documentation for np.choose.random. Look up the syntax on how to set the seed for the functions. Since the numpy function for the choose random requires an array a list was chosen to append the words from the dictionary. A simple math to get the probaility to determine a choose random number was also needed and formulated in the list determined by the number of values and variables. 

## Reflection 

The difficulty for the project is that how to iterate over the dictionary of dictionary in order to pull the next word that was needed. There was possibility of having different n order so the code needed to take account both a string and a tuple. What I thought the final function generate_random_text would have been a straight forward problem via trial and error with accounting for a certain number of loop rather than going through the markov text was chosen. There was also the dilemma for '*S*' and '*E*' computing into the output which doesnt match any of the scentences being formulated. 


## Appendix 

Gafurov, A., Brejová, B., & Medvedev, P. (2022). Markov chains improve the significance computation of overlapping genome annotations. Bioinformatics, 38(Supplement_1), i203–i211. https://doi.org/10.1093/bioinformatics/btac255




