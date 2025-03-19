# Project 8: Hidden Markov Models - Viterbi Algorithm
## Description

The Hidden Markov Model using the Viterbi algorithm offers an efficient method for path-finding through systems of hidden states. The algorithm developed will accomplish efficient path finding, log-space computation, and traceback mechanism. The algorithm is applied to gene finding determines the best path with the probabilities of transition states and the inital state. 

## Documentation and Usage

Python ver. 3.13
To run the program open the program with a Python IDE or via the terminal.

## Pseudocode
Explore different data structures to make the calculations easier.
### Initialization
- Grab list for states and length of the `obs`
- Calculate probabilities with `init_prob` and `emit_probs` by the state and obs for the first iteration, this will be used to fill in the rest of the matrix during recursion
### Recursion
- Nested for loop for sure to interate through the data structure
- Calculation is accomplished by the previous state * transition state * emission state based on the observation
### Termination
- Use `max` to get the highest scores from the states
### Traceback Step
- Set range and reverse order by 1 using first index
- Make current and next variables going through the state steps
## Reflection
Not having any pseudocode for the this project made us feel very lost. Lots of extra research was required to also grasp the concepts. The math was easy to follow but the reasoning portion of understanding needed extra exposure. Implementation was very difficult due to the freedom of options. Deciding whether to use the possible data structure options to organize the matrix was overwhelming. The resource in the appendix by GeekforGeeks provided good guidance on the direction of the project. 
## Citation
1. Chung, K. (2017). Viterbi Algorithm Explained. YouTube. https://www.youtube.com/watch?v=6JVqutwtzmo
2. GeeksforGeeks. (2024). Viterbi Algorithm for Hidden Markov Models (HMMs). Retrieved from https://www.geeksforgeeks.org/viterbi-algorithm-for-hidden-markov-models-hmms/
