from hmmlearn import hmm
import numpy as np

states = ["Sunny", "Rainy"]
observations = ["Walk", "Shop", "Clean"]

start_prob = np.array([0.7, 0.3])
trans_mat = np.array([
    [0.8, 0.2],
    [0.3, 0.7]
])
emit_mat = np.array([
    [0.6, 0.3, 0.1],
    [0.1, 0.4, 0.5]
])

# Build the model
model = hmm.MultinomialHMM(n_components=2, n_iter=100, init_params="")
model.startprob_ = start_prob
model.transmat_ = trans_mat
model.emissionprob_ = emit_mat

# Observation sequence as counts (2D array)
obs_seq = np.array([
    [1, 0, 0],  # Walk
    [0, 1, 0],  # Shop
    [0, 0, 1],  # Clean
    [0, 1, 0],  # Shop
    [1, 0, 0]   # Walk
])

# Set n_trials = sum of counts per observation
model.n_trials = obs_seq.sum(axis=1)

# Decode using Viterbi
logprob, hidden_states = model.decode(obs_seq, algorithm="viterbi")

print("Observed sequence:", [observations[np.argmax(o)] for o in obs_seq])
print("Most likely hidden states:", [states[i] for i in hidden_states])
print("Log probability:", logprob)
