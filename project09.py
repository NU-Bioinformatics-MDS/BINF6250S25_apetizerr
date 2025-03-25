"""
Forward, Backward, and Forward-Backward algorithms for HMMs

Algorithm Structure:

Forward Algorithm:
    Initialize with initial probabilities and the first observation
    Recursively calculate joint probabilities by summing over all possible previous states
    Compute total sequence probability by summing the final column
Backward Algorithm:
    Initialize final position with value 1 for all states
    Recursively calculate conditional probabilities working from end to beginning
    Combine with initial probabilities to get sequence likelihood
Forward-Backward Algorithm:
    Calculate both forward and backward matrices
    Combine to compute the posterior marginal probability for each state at each position
    Normalize to ensure valid probability distribution
"""


def forward(observation, initial_probs, transition_probs, emission_probs):
    """
    Gets the probabilities and states from the Hidden Markov Model and finds the forward sum probability and the forward matrix.

    :param observation: observation sequence
    :type observation: str
    :param initial_probs: initial probabilities for each state
    :type initial_probs: dict
    :param transition_probs: transition probabilities between states
    :type transition_probs: dict
    :param emission_probs: emission probabilities for each state
    :type emission_probs: dict
    :return: forward sequence probability and forward matrix
    :rtype: tuple(float, list[dict])
    """

    n_obs = len(observation)
    V = [{} for _ in range(n_obs)]
    states = [state for state in initial_probs.keys()]
    prev_states = states[::-1]

    # Initialization step for sum calculation
    for state in states:
        V[0][state] = initial_probs[state] * \
            emission_probs[state].get(observation[0])

    # forward recursion
    for nuc_position in range(1, n_obs):
        for state, prev_state in states, prev_states:
            probability1 = V[nuc_position - 1][state] * emission_probs[state].get(
                observation[nuc_position]) * transition_probs[state][state]

            probability2 = V[nuc_position - 1][prev_state] * transition_probs[prev_state][state] * emission_probs[state].get(
                observation[nuc_position], 0)

            V[nuc_position][state] = probability1 + probability2

    prob_sum = sum([V[-1][state] for state in states])
    return prob_sum, V


def backward(observation, initial_probs, transition_probs, emission_probs):
    """
    Gets the probabilities and states from the Hidden Markov Model and finds the backward sum probability and the backward matrix.

    :param observation: observation sequence
    :type observation: str
    :param initial_probs: initial probabilities for each state
    :type initial_probs: dict
    :param transition_probs: transition probabilities between states
    :type transition_probs: dict
    :param emission_probs: emission probabilities for each state
    :type emission_probs: dict
    :return: sequence likelihood and backward matrix
    :rtype: tuple(float, list[dict])
    """
    # last one is not calculated so a space is added to the front for the calculation
    n_obs = len(observation)
    observation = " " + observation[::-1]
    V = [{} for _ in range(n_obs)]
    states = [state for state in initial_probs.keys()]
    prev_states = states[::-1]

    # initialization step
    for state in states:
        V[0][state] = 1

    # backward calculation
    for nuc_position in range(1, n_obs):
        for state, prev_state in states, prev_states:
            prob1 = V[nuc_position - 1][state] \
                * emission_probs[state].get(observation[nuc_position], 0) \
                * transition_probs[state][state]

            prob2 = V[nuc_position - 1][prev_state] \
                * emission_probs[prev_state].get(observation[nuc_position], 0) \
                * transition_probs[state][prev_state]

            V[nuc_position][state] = prob1 + prob2

    # grabs the first initial probability and first emission nuceotide
    seq_likelihood_list = []
    for state in states:
        seq_likelihood_list.append(
            V[-1][state] * initial_probs[state] * emission_probs[state].get(observation[-1]))

    return sum(seq_likelihood_list), V


def forward_backward(observation, initial_probs, transition_probs, emission_probs):
    """
    Forward-Backward algorithm to compute the posterior probabilities of states given an observation sequence.

    :param observation: observation sequence
    :type observation: str
    :param initial_probs: initial probabilities for each state
    :type initial_probs: dict
    :param transition_probs: transition probabilities between states
    :type transition_probs: dict
    :param emission_probs: emission probabilities for each state
    :type emission_probs: dict
    :return: posterior probabilities for each state at each position
    :rtype: list[dict]
    """
    # run the forward algorithm; returns final sum and the forward matrix
    _, forward_matrix = forward(observation, initial_probs,
                                transition_probs, emission_probs)
    # run the backward algorithm; returns sequence likelihood and the backward matrix
    _, backward_matrix_reversed = backward(
        observation, initial_probs, transition_probs, emission_probs)

    # reverse the backward matrix so indexing matches the forward matrix
    # backward() modifies the observation order; we'll reverse its matrix before combining.
    backward_matrix = backward_matrix_reversed[::-1]

    states = list(initial_probs.keys())
    n_obs = len(observation)

    # compute posterior probabilities for each position
    posterior = []
    for t in range(n_obs):
        # sum of forward[t][s] * backward[t][s] over all states
        denom = sum(forward_matrix[t][s] *
                    backward_matrix[t][s] for s in states)
        gamma_t = {}

        for s in states:
            gamma_t[s] = (forward_matrix[t][s] * backward_matrix[t][s]) / \
                denom if denom else 0
        posterior.append(gamma_t)

    return posterior


def main():
    # Example observation sequence
    obs = "ATGCAA"

    # Example initial probabilities (probability of starting in each state)
    init_probs = {
        "E": 0.6,
        "I": 0.4
    }

    # Example transition probabilities (probability of moving from one state to another)
    trans_probs = {
        "E": {"E": 0.8, "I": 0.2},
        "I": {"E": 0.3, "I": 0.7}
    }

    # Example emission probabilities (probability of observing a symbol in a given state)
    emit_probs = {
        "E": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3},
        "I": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1}
    }

    # Run the Forward algorithm
    forward_prob, forward_matrix = forward(
        obs, init_probs, trans_probs, emit_probs)
    print("Forward Probability:", forward_prob)
    print("Forward Matrix:")
    for t, state_probs in enumerate(forward_matrix):
        print(f"Time {t}: {state_probs}")
    print()

    # Run the Backward algorithm
    backward_prob, backward_matrix = backward(
        obs, init_probs, trans_probs, emit_probs)
    print("Backward Probability:", backward_prob)
    print("Backward Matrix:")
    for t, state_probs in enumerate(backward_matrix):
        print(f"Time {t}: {state_probs}")
    print()

    # Run the Forward-Backward algorithm
    posterior_probs = forward_backward(
        obs, init_probs, trans_probs, emit_probs)
    print("Posterior Probabilities:")
    for t, state_probs in enumerate(posterior_probs):
        print(f"Time {t}: {state_probs}")
    print()


if __name__ == '__main__':
    main()
