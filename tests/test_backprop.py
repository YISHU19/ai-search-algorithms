import unittest

from neural.backprop import forward, initial_params, sigmoid, train_step


class TestBackprop(unittest.TestCase):
    def test_sigmoid(self):
        self.assertAlmostEqual(sigmoid(0), 0.5)

    def test_forward_pass_matches_worked_example(self):
        weights, biases = initial_params()
        out = forward((1, 0, 1), weights, biases)
        self.assertAlmostEqual(out[4], 0.332, places=3)
        self.assertAlmostEqual(out[5], 0.525, places=3)
        self.assertAlmostEqual(out[6], 0.4739, places=4)

    def test_one_update_moves_output_towards_target(self):
        weights, biases = initial_params()
        train_step((1, 0, 1), 1, weights, biases)
        self.assertAlmostEqual(forward((1, 0, 1), weights, biases)[6], 0.5152, places=4)

    def test_repeated_training_converges(self):
        weights, biases = initial_params()
        for _ in range(500):
            train_step((1, 0, 1), 1, weights, biases)
        self.assertGreater(forward((1, 0, 1), weights, biases)[6], 0.95)


if __name__ == "__main__":
    unittest.main()
