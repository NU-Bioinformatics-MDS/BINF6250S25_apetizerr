# Project 9: Forward, Backward, and Forward-Backward Algorithms
## Description
The program contains 3 algorithm that are dynamically applied to probabilistic states of nucleotide, transition and initial state. This program is able to calculate the sequence likelihoods and posterior probabilities. The Forward Algorithm computes the joint probability by summing the previous and partial observations. The Backward Algorithm is able to predict the future observation given the current state. Then the Forward-Backward Algorithm combines both to find the probability of each state at the current position of the observation sequence.
## Documentation and Usage

Python ver. 3.13
To run the program open the program with a Python IDE or via the terminal.

## Pseudocode
The data structure to store the different states in the matrix used list of dictionaries.
### Forward Algorithm
- Grab list for states and length of the `obs`
- Get the previous observation summed score or initialized score to use as a multiplier for the current state nucleotide obervation, and the transitions states
- sum the other transition state score
- Finalize by getting the last scores as a sum
  
### Backward Algorithm
- Initialize the final probability for 1 for the states
- calculate getting the preivous and the last transition state with the nucleotide probability and adding the alternate state
- Use the inital probability to multiply the final result and the last nucleotide probability 
  
### Forward-Backward Algorithm
- Call the implemented functions for both previously made algorithm
- Combine both to get the posterior marginal probability

  
## Reflection

While coding for the forward and backward it was difficult to ensure the right calculation is being accomplished. So to ensure calculation were correct we manually calculated the algorithms intended output to match if the direction was on the right path. This made testing and reruning the code easier making print statements to know which calculation wasn't functioning. Another struggle throughout the project would be working around the Key Error. When iterating through the dictionary to find the state there were errors even through manually inputing the state seperatly from the for loop worked. The problem was resolved but not fully understood why Python behaved that way. Calculating the initial probabilities were also hard to understand at the end of the backward algorithm requiring extra research to ensure the final output was correct. 

## Citation
1. GeeksforGeeks. (2024). Viterbi Algorithm for Hidden Markov Models (HMMs). Retrieved from https://www.geeksforgeeks.org/viterbi-algorithm-for-hidden-markov-models-hmms/
