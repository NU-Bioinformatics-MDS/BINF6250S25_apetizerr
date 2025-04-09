# Project 10: Baum-Welch Algorithm for Hidden Markov Model
## Description

The Baum-Welch Algorithm is an expectation maximization approach for HMM parameters. Using the forward and backward algorithm, the predicted statistic from each observation is used to find the parameters of HMM. By doing so this application of unsupervised learning is used to train a models for examples like CpG island detection, coding regions of bacteria and gene prediction. The model takes observations of a sequence, initial probabilities, transition probabilities and emission probabilities and gives the updated version based on the observation and statistics. 
## Documentation and Usage
- Python ver: 1.13
- Packages: math
Run program in the terminal or open and use in an IDE. 
Have the inputs as a dictionary of dictionary as the data structure.
Edit the global variables within the code `maxIter = 100` for the number of iteration and `epsilon = 1e-4` as the convergence threshold.
## Pseudocode
```
Algorithm BaumWelch(obs, init_probs, trans_probs, emit_probs, maxIter, epsilon)
    Input:
        obs: List of observed sequences (e.g., ["GGCACTGAA", "ATGCAATGC", "AATGCCTGA"])
        init_probs: Dictionary of initial state probabilities (e.g., {"H": 0.5, "L": 0.5})
        trans_probs: Dictionary of transition probabilities (e.g., {"H": {"H": 0.6, "L": 0.4}, "L": {"H": 0.3, "L": 0.7}})
        emit_probs: Dictionary of emission probabilities (e.g., {"H": {"A": 0.2, "C": 0.3, "G": 0.3, "T": 0.2}, "L": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3}})
        maxIter: Maximum number of iterations
        epsilon: Convergence threshold (change in log-likelihood)

    Output:
        Updated init_probs, trans_probs, emit_probs

    prevLogLikelihood = -∞

    For iter = 1 to maxIter do:
        // Initialize accumulators for expected counts
        expected_init = {state: 0 for each state in init_probs}
        expected_trans = {state: {next_state: 0 for each next_state in trans_probs[state]} for each state in trans_probs}
        expected_emit = {state: {symbol: 0 for each symbol in emit_probs[state]} for each state in emit_probs}
        total_gamma = {state: 0 for each state in init_probs}
        total_logLikelihood = 0

        For each sequence in obs do:
            T = length(sequence)

            // --- E-Step: Compute probabilities using provided routines ---
            // Use existing implementations for Forward and Backward computations.
            alpha = Forward(sequence, init_probs, trans_probs, emit_probs)
            beta  = Backward(sequence, trans_probs, emit_probs)

            // Calculate likelihood of the sequence
            seqLikelihood = sum(alpha[T][state] for each state in init_probs)
            total_logLikelihood = total_logLikelihood + log(seqLikelihood)

            // Compute gamma: probability of being in a state at time t
            For t = 1 to T do:
                For each state in init_probs do:
                    gamma[t][state] = (alpha[t][state] * beta[t][state]) / seqLikelihood
                EndFor
            EndFor

            // Compute xi: probability of transitioning from state i to state j at time t
            For t = 1 to T - 1 do:
                For each state in init_probs do:
                    For each next_state in init_probs do:
                        xi[t][state][next_state] = (alpha[t][state] *
                                                    trans_probs[state][next_state] *
                                                    emit_probs[next_state][sequence[t+1]] *
                                                    beta[t+1][next_state]) / seqLikelihood
                    EndFor
                EndFor
            EndFor

            // Accumulate expected counts for the initial state probabilities
            For each state in init_probs do:
                expected_init[state] = expected_init[state] + gamma[1][state]
            EndFor

            // Accumulate expected counts for transitions and state occupancy (for emissions)
            For t = 1 to T - 1 do:
                For each state in init_probs do:
                    total_gamma[state] = total_gamma[state] + gamma[t][state]
                    For each next_state in init_probs do:
                        expected_trans[state][next_state] = expected_trans[state][next_state] + xi[t][state][next_state]
                    EndFor
                EndFor
            EndFor

            // Accumulate expected counts for emissions (include time step T)
            For t = 1 to T do:
                symbol = sequence[t]   // current observed symbol
                For each state in init_probs do:
                    expected_emit[state][symbol] = expected_emit[state][symbol] + gamma[t][state]
                EndFor
            EndFor

        EndFor  // End processing all sequences

        // --- M-Step: Update model parameters based on expected counts ---

        // Update initial state probabilities
        For each state in init_probs do:
            init_probs[state] = expected_init[state] / (number of sequences)
        EndFor

        // Update transition probabilities
        For each state in trans_probs do:
            For each next_state in trans_probs[state] do:
                trans_probs[state][next_state] = expected_trans[state][next_state] / total_gamma[state]
            EndFor
        EndFor

        // Update emission probabilities
        For each state in emit_probs do:
            total_emissions = sum(expected_emit[state][symbol] for each symbol in emit_probs[state])
            For each symbol in emit_probs[state] do:
                emit_probs[state][symbol] = expected_emit[state][symbol] / total_emissions
            EndFor
        EndFor

        // Optional: Include scaling in the Forward and Backward routines to prevent numerical underflow

        // Check for convergence based on change in log-likelihood
        If |total_logLikelihood - prevLogLikelihood| < epsilon then:
            Break the loop
        EndIf

        prevLogLikelihood = total_logLikelihood
    EndFor

    Return init_probs, trans_probs, emit_probs
```
 
## Reflection

The math and reasoning for each step was difficult to comprehend needing different sources of explaination even if the full process was provided. 
We ran into the issue of very small numbers from the forward and backward algorithms. Due to multiplication of very small numbers leading to numerical overflow we used scaling to normalize the probabilities at each step to keep them in manageable numerical range. There were a lot of for loop making it difficult to keep track and planning for the potential errors were also difficult to troubleshoot. 

## Appendix
- Mills, R. (n.d.). Baum-Welch EM Algorithm. University of Michigan.
- Compeau, P., & Pevzner, P. (2014). Bioinformatics algorithms: An active learning approach. San Diego, CA: Active Learning Publishers.
- Rabiner, L. R. (1989). A tutorial on hidden Markov models and selected applications in speech recognition. Proceedings of the IEEE, 77(2), 257–286. https://doi.org/10.1109/5.18626
