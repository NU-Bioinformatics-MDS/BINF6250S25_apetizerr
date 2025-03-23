import numpy as np
# Example observation sequence
obs = "ATGCAA"

# Example initial probabilities (probability of starting in each state: E := Exon, I := Intron)
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

def forward(observation,
            initial_probability,
            transition_probs,
            emission_probs):
    """
    Gets the probabilities and states from the Hidden Markov Model and finds the forward sum probability
    @param observation:
    @param initial_probability:
    @param transition_probs:
    @param emission_probs:
    @return:
    """

    n_obs = len(observation)
    V = [{} for _ in range(n_obs)]
    states = [state for state in initial_probability.keys()]
    prev_states = states[::-1]

    # Initialization step for sum calculation
    for state in states:
        V[0][state] = initial_probability[state] * emission_probs[state].get(observation[0])
    # forward recursion
    for nuc_position in range(1, n_obs):
        for state, prev_state in states, prev_states:
                probability1 = V[nuc_position - 1][state] * emission_probs[state].get(observation[nuc_position]) * transition_probs[state][state]

                probability2 = V[nuc_position - 1][prev_state] * transition_probs[prev_state][state] * emission_probs[state].get(
                    observation[nuc_position], 0)
                V[nuc_position][state] = probability1 + probability2
    print(V)
    prob_sum = sum([V[-1][state] for state in states])
    return prob_sum


def backward(observation,
            initial_probability,
            transition_probs,
            emission_probs):
    # last one is not calculated so a space is added to the front for the calculation
    n_obs = len(observation)
    observation = " " + observation[::-1]
    V = [{} for _ in range(n_obs)]
    states = [state for state in initial_probability.keys()]
    prev_states = states[::-1]
    # initialization step
    for state in states:
        V[0][state] = 1

    # backward calculation
    for nuc_position in range(1, n_obs):
        for state, prev_state in states, prev_states:
            prob1 = V[nuc_position - 1][state] * emission_probs[state].get(observation[nuc_position]) * transition_probs[state][state]

            prob2 = V[nuc_position - 1][prev_state] * emission_probs[prev_state].get(observation[nuc_position]) * transition_probs[state][prev_state]

            V[nuc_position][state] = prob1 + prob2

    # grabs the first initial probability and first emission nuceotide
    seq_likelihood_list = []
    for state in states:
        seq_likelihood_list.append(V[-1][state] * initial_probability[state] * emission_probs[state].get(observation[-1]))
    return sum(seq_likelihood_list)

