# Waterman Smith Project

## Description of the project
This project recreates a simple Smith Waterman algorithm employing a local alignment scoring method. The program attempts to apply dynamic programming between two DNA strings. The program reconstructs the DNA sequence using the algorithm using two matrix: one for the scoring and the other for tracing the steps to assemble the DNA. This iterates through the matrix by scoring each nucelotide to determine the scoring algorithim and the direction. With this scoring, we can trace back the directions one took with the two sequences. The process involves iterating through the matrix while scoring each nucleotide match, mismatch, and gap to determine the local alignment. 

## Pertinent documentation and usage write-up
- Python ver. 3.13
- Packages: Numpy
Run the program on a terminal or IDE with Python and ensure the packages are installed before running the script.

## Pseudocode
First numpy array and documentation for matrix is reviewed. Iterating through the row and column one by one with a for loop is needed then with each iteration the score taken from the matrix score diagnally, left side and the top is taken account and the max is given.

## Reflection
For the `max_score` function there were conditions potentially when the max would be the same as the diagnol at 0. We concluded when the diagnol and the other calculation were equal the diagnol will be the chosen max. The traceback matrix was conceptually difficult to grasp thinking of numbers as directions. It was a two part problem of understanding the numbers in the matrix then using that information to append a gap or a nucleotide for the aligned output sequence.

## Appendix
Compeau, P., & Pevzner, P. (2018). Bioinformatics algorithms: An active learning approach (3rd ed.). Active Learning Publishers.
Spiceworks. (n.d.). What is dynamic programming? Spiceworks. Retrieved February 11, 2025, from https://www.spiceworks.com/tech/devops/articles/what-is-dynamic-programming/

