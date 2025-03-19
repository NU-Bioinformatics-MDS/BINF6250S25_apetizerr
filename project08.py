"""
Viterbi Algorithm

Algorithm Structure:

1. Initialization:
    - Set up a probability matrix using initial probabilities and the first observation
    - Initialize traceback matrix for path reconstruction
2. Recursion:
    - For each position and possible state, calculate the maximum probability
    - Store both probabilities and traceback pointers
    - Apply transition and emission probabilities at each step
3. Termination:
    - Identify the final state with the highest probability
    - Trace back through the matrix to reconstruct the optimal path
"""

import numpy as np


def safe_log(p, epsilon=1e-10):
    """
    Safe log function to avoid log(0) issues
    """
    return np.log(p) if p > 0 else np.log(epsilon)


def viterbi_algorithm(states, obs, init_probs, trans_probs, emit_probs):
    """
    Implements the Viterbi algorithm to find the most probable sequence of states
    given a sequence of observations and a Hidden Markov Model (HMM).

    :param states: possible states in the HMM
    :type states: list
    :param obs: observed sequence of symbols
    :type obs: str
    :param init_probs: initial probabilities for each state
    :type init_probs: dict
    :param trans_probs: transition probabilities between states
    :type trans_probs: dict
    :param emit_probs: emission probabilities for each state
    :type emit_probs: dict
    """
    n_obs = len(obs)
    epsilon = 1e-10  # pseudocount to avoid log(0)

    # initialize the probability and traceback matrices
    V = [{} for _ in range(n_obs)]
    T = [{} for _ in range(n_obs)]

    # initialization step
    for state in states:
        V[0][state] = safe_log(init_probs[state]) + \
            safe_log(emit_probs[state].get(obs[0], epsilon))
        T[0][state] = None

    # recursion step
    for t in range(1, n_obs):
        for state in states:

            # find the previous state that maximizes the probability
            best_prob = -np.inf
            best_prev_state = None
            for prev_state in states:
                prob = (V[t - 1][prev_state] +
                        safe_log(trans_probs[prev_state][state]) +
                        safe_log(emit_probs[state].get(obs[t], epsilon)))
                if prob > best_prob:
                    best_prob = prob
                    best_prev_state = prev_state

            # store the best probability and traceback pointer
            V[t][state] = best_prob
            T[t][state] = best_prev_state

    # termination step
    max_final_prob, last_state = max(
        ((V[n_obs - 1][state], state) for state in states),
        key=lambda x: x[0]
    )

    # traceback step
    best_path = []
    current_state = last_state

    # reconstruct the optimal path
    for t in range(n_obs - 1, -1, -1):
        best_path.insert(0, current_state)
        current_state = T[t][current_state]

    return best_path, np.exp(max_final_prob)


def main():
    # Example observation sequence
    obs = "GGCACTGAA"

    # Example initial probabilities (probability of starting in each state)
    init_probs = {
        "I": 0.2,
        "G": 0.8
    }

    # Example states
    states = [state for state in init_probs.keys()]

    # Example transition probabilities (probability of moving from one state to another)
    trans_probs = {
        "I": {"I": 0.7, "G": 0.3},
        "G": {"I": 0.1, "G": 0.9}
    }

    # Example emission probabilities (probability of observing a symbol in a given state)
    emit_probs = {
        "I": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
        "G": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3}
    }

    # Run the Viterbi algorithm
    best_path, max_final_prob = viterbi_algorithm(states,
                                                  obs,
                                                  init_probs,
                                                  trans_probs,
                                                  emit_probs)

    # Print the results
    print("Most probable path:", best_path)
    print("Max probability:", max_final_prob)


if __name__ == '__main__':
    main()
