import math


def forward(observation,
            initial_probability,
            transition_probs,
            emission_probs):
    """
    Computes and returns the full forward probability table (alpha) for the observation sequence.

    @param observation: String containing observed symbols e.g. "GGCACTGAA"
    @param initial_probability: Dictionary of initial probabilities for each state.
    @param transition_probs: Nested dictionary of transition probabilities.
    @param emission_probs: Nested dictionary of emission probabilities.
    @return: List of dictionaries representing the alpha table.
    """

    n_obs = len(observation)
    alpha = [{} for _ in range(n_obs)]
    states = list(initial_probability.keys())
    c = [0] * n_obs  # Scaling factors

    # Initialization step with scaling
    c[0] = 0
    for state in states:
        alpha[0][state] = initial_probability[state] * \
            emission_probs[state].get(observation[0], 0)
        c[0] += alpha[0][state]
    # Scale alpha[0]
    c[0] = 1 / c[0] if c[0] != 0 else 1
    for state in states:
        alpha[0][state] *= c[0]

    # Forward recursion with scaling at each time step
    for t in range(1, n_obs):
        c[t] = 0
        for state in states:
            alpha[t][state] = sum(alpha[t-1][prev_state] * transition_probs[prev_state][state] for prev_state in states) \
                * emission_probs[state].get(observation[t], 0)
            c[t] += alpha[t][state]
        # Scale alpha[t]
        c[t] = 1 / c[t] if c[t] != 0 else 1
        for state in states:
            alpha[t][state] *= c[t]

    return alpha, c


def backward(observation,
             initial_probability,
             transition_probs,
             emission_probs,
             c):
    """
    Computes and returns the full backward probability table (beta) for the observation sequence.

    @param observation: String containing observed symbols (e.g., "GGCACTGAA")
    @param initial_probability: Dictionary of initial state probabilities.
    @param transition_probs: Nested dictionary of transition probabilities.
    @param emission_probs: Nested dictionary of emission probabilities.
    @return: List of dictionaries representing the backward table.
    """
    n_obs = len(observation)
    beta = [{} for _ in range(n_obs)]
    states = list(initial_probability.keys())

    # Initialization step: scale last beta by the factor from forward pass
    for state in states:
        beta[n_obs - 1][state] = c[n_obs - 1]   # typically β[T-1] = c[T-1]

    # Backward recursion with scaling
    for t in range(n_obs - 2, -1, -1):
        for state in states:
            beta[t][state] = sum(transition_probs[state][next_state] *
                                 emission_probs[next_state].get(observation[t+1], 0) *
                                 beta[t+1][next_state] for next_state in states)
            beta[t][state] *= c[t]  # apply scaling factor for time t
    return beta


def baumwelch(obs, init_probs, trans_probs, emit_probs, maxIter, epsilon):
    """
    Implements the Baum-Welch algorithm for training a Hidden Markov Model (HMM).

    @param obs: List of observation sequences (each sequence is a string).
    @init_probs: Dictionary of initial state probabilities.
    @trans_probs: Nested dictionary of transition probabilities.
    @emit_probs: Nested dictionary of emission probabilities.
    @maxIter: Maximum number of iterations for the algorithm.
    @epsilon: Convergence threshold for log-likelihood.
    @return: Updated initial probabilities, transition probabilities, and emission probabilities.
    """

    prevLogLikelihood = float('-inf')

    # Initialize accumulators for expected counts
    for _ in range(maxIter):
        expected_init = {state: 0 for state in init_probs}
        expected_trans = {state: {
            next_state: 0 for next_state in trans_probs[state]} for state in trans_probs}
        expected_emit = {
            state: {symbol: 0 for symbol in emit_probs[state]} for state in emit_probs}
        total_gamma = {state: 0 for state in init_probs}
        total_logLikelihood = 0

        # --- E-Step: Expectation step to compute expected counts ---

        # Process each observation sequence
        for seq in obs:
            T = len(seq)

            # Compute forward and backward tables (assumed to return dictionaries indexed 1..T)
            alpha, c = forward(seq, init_probs, trans_probs, emit_probs)
            beta = backward(seq, init_probs, trans_probs, emit_probs, c)

            # Calculate likelihood of the sequence
            seqLikelihood = sum(alpha[T-1][state] for state in init_probs)
            total_logLikelihood += math.log(seqLikelihood)

            # Initialize and compute gamma and xi arrays in a single pass
            gamma = {t: {} for t in range(T)}  # Use 0-based indexing
            xi = {t: {state: {next_state: 0 for next_state in init_probs} for state in init_probs}
                  for t in range(T-1)}  # Use 0-based indexing for xi

            for t in range(T):  # Loop from 0 to T-1
                for state in init_probs:
                    gamma[t][state] = (alpha[t][state] *
                                       beta[t][state]) / seqLikelihood
                    if t < T-1:  # Compute xi only for t = 0 to T-2
                        for next_state in init_probs:
                            xi[t][state][next_state] = (alpha[t][state] *
                                                        trans_probs[state][next_state] *
                                                        emit_probs[next_state][seq[t+1]] *
                                                        beta[t+1][next_state]) / seqLikelihood

            # Accumulate expected counts for initial state probability, transitions, and emissions
            for t in range(T):
                symbol = seq[t]
                for state in init_probs:
                    if t == 0:  # Initial state probability
                        expected_init[state] += gamma[t][state]
                    total_gamma[state] += gamma[t][state]  # State occupancy

                    # Emissions
                    expected_emit[state][symbol] += gamma[t][state]
                    if t < T - 1:  # Transitions (only for t = 0 to T-2)
                        for next_state in init_probs:
                            expected_trans[state][next_state] += xi[t][state][next_state]

        # --- M-Step: Update parameters based on expected counts ---

        # Update initial probabilities (weighted by the number of sequences)
        nSeq = len(obs)
        for state in init_probs:
            init_probs[state] = expected_init[state] / nSeq

        # Update transition probabilities
        for state in trans_probs:
            for next_state in trans_probs[state]:

                # Guard against division by zero
                if total_gamma[state] > 0:
                    trans_probs[state][next_state] = expected_trans[state][next_state] / \
                        total_gamma[state]
                else:
                    trans_probs[state][next_state] = 0

        # Update emission probabilities
        for state in emit_probs:
            total_emissions = sum(
                expected_emit[state][symbol] for symbol in emit_probs[state])
            for symbol in emit_probs[state]:

                # Guard against division by zero
                if total_emissions > 0:
                    emit_probs[state][symbol] = expected_emit[state][symbol] / \
                        total_emissions
                else:
                    emit_probs[state][symbol] = 0

        # Check for convergence based on change in log-likelihood
        if abs(total_logLikelihood - prevLogLikelihood) < epsilon:
            break

        prevLogLikelihood = total_logLikelihood

    return init_probs, trans_probs, emit_probs


def main():
    # Example observation sequences (multiple sequences for training)
    obs = ["GGCACTGAA", "ATGCAATGC", "AATGCCTGA"]

    # Example initial probabilities (probability of starting in each state)
    init_probs = {
        "H": 0.5,  # H = High GC content state
        "L": 0.5   # L = Low GC content state
    }

    # Example transition probabilities (probability of moving from one state to another)
    trans_probs = {
        "H": {"H": 0.6, "L": 0.4},
        "L": {"H": 0.3, "L": 0.7}
    }

    # Example emission probabilities (probability of observing a symbol in a given state)
    emit_probs = {
        "H": {"A": 0.2, "C": 0.3, "G": 0.3, "T": 0.2},
        "L": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3}
    }

    # Parameters for the Baum-Welch algorithm
    maxIter = 100
    epsilon = 1e-4

    # Run the Baum-Welch algorithm
    updated_init_probs, updated_trans_probs, updated_emit_probs = baumwelch(
        obs, init_probs, trans_probs, emit_probs, maxIter, epsilon)

    print("Updated Initial Probabilities:")
    print(updated_init_probs)
    print("\nUpdated Transition Probabilities:")
    print(updated_trans_probs)
    print("\nUpdated Emission Probabilities:")
    print(updated_emit_probs)


if __name__ == "__main__":
    main()
