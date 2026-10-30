"""Backpropagation by hand on a tiny 3-2-1 network.

Inputs x1..x3 feed hidden units 4 and 5, which feed output unit 6. All units
use the sigmoid activation. This is the classic worked example from data
mining textbooks: one forward pass, one weight update, and the forward pass
again to show the output moving towards the target.
"""

import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def initial_params():
    """Weights w[i, j] (from unit i to unit j) and biases theta[j]."""
    weights = {
        (1, 4): 0.2, (1, 5): -0.3,
        (2, 4): 0.4, (2, 5): 0.1,
        (3, 4): -0.5, (3, 5): 0.2,
        (4, 6): -0.3, (5, 6): -0.2,
    }
    biases = {4: -0.4, 5: 0.2, 6: 0.1}
    return weights, biases


def forward(x, weights, biases):
    """Return the activations of every unit, keyed by unit number."""
    out = {1: x[0], 2: x[1], 3: x[2]}
    for j in (4, 5):
        out[j] = sigmoid(sum(out[i] * weights[i, j] for i in (1, 2, 3)) + biases[j])
    out[6] = sigmoid(out[4] * weights[4, 6] + out[5] * weights[5, 6] + biases[6])
    return out


def train_step(x, target, weights, biases, learning_rate=0.9):
    """Do one backpropagation update in place and return the errors per unit."""
    out = forward(x, weights, biases)

    # Output error, then hidden errors using the weights *before* the update
    err = {6: out[6] * (1 - out[6]) * (target - out[6])}
    for j in (4, 5):
        err[j] = out[j] * (1 - out[j]) * err[6] * weights[j, 6]

    for (i, j) in weights:
        weights[i, j] += learning_rate * err[j] * out[i]
    for j in biases:
        biases[j] += learning_rate * err[j]
    return err


def main():
    x, target = (1, 0, 1), 1
    weights, biases = initial_params()

    before = forward(x, weights, biases)[6]
    train_step(x, target, weights, biases)
    after = forward(x, weights, biases)[6]

    print(f"Output before update: {before:.4f}")
    print(f"Output after update:  {after:.4f}  (target {target})")


if __name__ == "__main__":
    main()
