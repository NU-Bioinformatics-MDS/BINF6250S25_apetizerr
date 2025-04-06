import math
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


def baumwelch(obs, init_probs, trans_probs, emit_probs, maxIter, epsilon):

    prevLogLikelihood = float('-inf')

    for iter in range(maxIter):
        expected_init = {state: 0 for state in init_probs}
        expected_trans = {state: {next_state: 0 for next_state in trans_probs[state]} for
                          state in trans_probs}
        expected_emit = {state: {symbol: 0 for symbol in emit_probs[state]} for state in emit_probs}
        total_gamma = {state: 0 for state in init_probs}
        total_logLikelihood = 0


        for seq in obs:
            T = len(seq)
            alpha = forward(seq, init_probs, trans_probs, emit_probs)
            beta = backward(seq, init_probs, trans_probs, emit_probs)
            seqLikelihood = sum(alpha[T][state] for state in init_probs)
            total_logLikelihood = total_logLikelihood + math.log(seqLikelihood)
            gamma = [{} for _ in range(T + 1)]

            for t in range(1, T + 1):
                for state in init_probs:
                    gamma[t][state] = (alpha[t][state] * beta[t][state]) / seqLikelihood
            xi = [ [ [0 for _ in init_probs] for _ in init_probs] for _ in range(T + 1)]

            for i, state in enumerate(init_probs):
                for j, next_state in enumerate(init_probs):
                    xi[t][i][j] = (alpha[t][state] *
                                   trans_probs[state][next_state] *
                                   emit_probs[state][seq[t]] * beta[t+1][next_state]) / seqLikelihood




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

print(forward(obs, init_probs, trans_probs, emit_probs))

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
